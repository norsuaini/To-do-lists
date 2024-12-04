require('dotenv').config(); // Load environment variables

const { Pool } = require("pg");

const pool = new Pool({
    user: process.env.DB_USER,
    host: process.env.DB_HOST,
    port: 5432,
    database: process.env.DB_NAME
});

// This function checks and creates the table if it doesn't exist
const createTableIfNotExists = async () => {
    const query = `
      CREATE TABLE IF NOT EXISTS todo (
        id SERIAL PRIMARY KEY,
        description TEXT NOT NULL
      );
    `;
    
    try {
      await pool.query(query);
      console.log("Table is ready or already exists.");
    } catch (err) {
      console.error("Error creating table: ", err.message);
    }
  };
  
  // Call the function to ensure the table is created
  createTableIfNotExists();

module.exports = pool;