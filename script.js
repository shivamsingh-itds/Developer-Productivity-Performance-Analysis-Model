const res = await fetch("https://your-api.onrender.com/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ experience: getVal('exp'), commits_per_week: getVal('commits'), ... })
});
const data = await res.json();
// use data.performance_score to drive the UI