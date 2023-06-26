const express = require("express");
const bodyParser = require("body-parser");
const sqlite3 = require("sqlite3").verbose();
const path = require("path");

const app = express();
const db = new sqlite3.Database("user-input.db");

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname)));

db.serialize(() => {
  db.run("CREATE TABLE IF NOT EXISTS user_input (input TEXT)");
});

app.post("/save-input", (req, res) => {
  const input = req.body.input;

  db.run("INSERT INTO user_input (input) VALUES (?)", [input], (err) => {
    if (err) {
      console.error(err);
      res.status(500).send("Error saving input.");
    } else {
      res.status(200).send("Input saved successfully.");
    }
  });
});

app.post("/pw", (req, res) => {
  const pw = req.body.pw;

  db.run("INSERT INTO user_input (input) VALUES (?)", [pw], (err) => {
    if (err) {
      console.error(err);
      res.status(500).send("Error saving input.");
    } else {
      res.status(200).send("Input saved successfully.");
    }
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
