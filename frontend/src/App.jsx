import { useState } from "react";

function App() {
  const [claim, setClaim] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const verifyClaim = async () => {
    if (!claim.trim()) return;

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await fetch("http://127.0.0.1:8000/verify", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          claims: [claim],
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || "Verification failed");
      }

      setResult(data.results[0]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.page}>
      {/* LEFT PANEL */}
      <div style={styles.card}>
        <h1 style={styles.title}>GuardianX</h1>
        <p style={styles.subtitle}>
          AI-powered misinformation & claim verification
        </p>

        <textarea
          value={claim}
          onChange={(e) => setClaim(e.target.value)}
          placeholder="Enter a claim to verify..."
          style={styles.textarea}
        />

        <button style={styles.button} onClick={verifyClaim} disabled={loading}>
          {loading ? "Verifying..." : "Verify Claim"}
        </button>

        {error && <p style={styles.error}>❌ {error}</p>}
      </div>

      {/* RIGHT PANEL */}
      <div style={styles.resultPanel}>
        {!result && !loading && (
          <p style={styles.placeholder}>
            Verification result will appear here
          </p>
        )}

        {result && (
          <div style={styles.resultCard}>
            <h3 style={styles.resultTitle}>Result</h3>
            <p><strong>Claim:</strong> {result.claim}</p>
            <p>
              <strong>Verdict:</strong>{" "}
              <span style={verdictStyle(result.verdict)}>
                {result.verdict}
              </span>
            </p>
            <p><strong>Explanation:</strong></p>
            <p style={styles.explanation}>{result.explanation}</p>
          </div>
        )}
      </div>
    </div>
  );
}

const verdictStyle = (verdict) => ({
  color:
    verdict === "TRUE"
      ? "#22c55e"
      : verdict === "FALSE"
      ? "#ef4444"
      : "#eab308",
  fontWeight: "700",
});

const styles = {
  page: {
    minHeight: "100vh",
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    background: "radial-gradient(circle at center, #0f172a 0%, #020617 70%)",
    color: "#fff",
    fontFamily: "Inter, sans-serif",
  },

  card: {
    margin: "auto",
    width: "100%",
    maxWidth: "520px",
    background: "rgba(255,255,255,0.05)",
    borderRadius: "20px",
    padding: "40px",
    backdropFilter: "blur(14px)",
    boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
    textAlign: "center",
  },

  title: {
    fontSize: "3rem",
    marginBottom: "10px",
  },

  subtitle: {
    opacity: 0.8,
    marginBottom: "30px",
  },

  textarea: {
    width: "100%",
    height: "120px",
    borderRadius: "12px",
    padding: "15px",
    fontSize: "16px",
    border: "none",
    outline: "none",
    marginBottom: "20px",
  },

  button: {
    padding: "12px 30px",
    borderRadius: "999px",
    border: "none",
    fontSize: "16px",
    fontWeight: "600",
    cursor: "pointer",
    background: "linear-gradient(90deg, #22d3ee, #6366f1)",
    color: "#020617",
  },

  error: {
    marginTop: "15px",
    color: "#f87171",
  },

  resultPanel: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "40px",
  },

  placeholder: {
    opacity: 0.5,
    fontSize: "18px",
  },

  resultCard: {
    maxWidth: "520px",
    background: "rgba(255,255,255,0.05)",
    padding: "30px",
    borderRadius: "20px",
    boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
  },

  resultTitle: {
    marginBottom: "15px",
  },

  explanation: {
    opacity: 0.9,
    lineHeight: 1.6,
  },
};

export default App;
