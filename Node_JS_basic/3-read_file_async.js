const fs = require('fs');

function countStudents(path) {
  return (new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, fileContent) => {
      if (!fs.existsSync(path)) {
        throw new Error('Cannot load the database');
      }

      if (err) {
        reject(err);
      }

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

      let output = `Number of students: ${students.length}\n`;

      for (const field in fields) {
        if (fields[field].length > 0) {
          const formattedList = fields[field].join(', ');
          output += `Number of students in ${field}: ${fields[field].length}. List: ${formattedList}\n`;
        }
      }
      resolve(output.trim());
    });
  }));
}

module.exports = countStudents;