const fs = require('fs');

function countStudents(path) {
  try {
    if (!fs.existsSync(path)) {
      throw new Error('Cannot load the database');
    }

    const fileContent = fs.readFileSync(path, { encoding: 'utf-8' }).trim();
    const lines = fileContent.split('\n').filter((line) => line);

    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    const students = [];
    const fields = {};

    for (let i = 1; i < lines.length; i += 1) {
      const row = lines[i].split(',');
      const [firstname, , , field] = row.map((col) => col.trim());

      if (firstname && field) {
        students.push({ firstname, field });
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    }

    console.log(`Number of students: ${students.length}`);

    for (const field in fields) {
      if (fields[field].length > 0) {
        const formattedList = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${formattedList}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;