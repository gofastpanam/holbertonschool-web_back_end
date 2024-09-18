const fs = require('fs');
const csv = require('csv-parser');

function countStudents(path) {
  return (new Promise((resolve, reject) => {
    if (!path) {
      reject(new Error('Cannot load the database'));
    }

    const students = [];
    let counter1 = 0;
    let counter2 = 0;
    const newList1 = [];
    const newList2 = [];
    const field1 = 'CS';
    const field2 = 'SWE';

    fs.createReadStream(path)
      .pipe(csv())
      .on('data', (row) => {
        students.push(row);
      })
      .on('end', () => {
        resolve(students);
        console.log(`Number of students: ${students.length}`);
        for (let i = 0; i < students.length; i += 1) {
          if (students[i].field === field1) {
            counter1 += 1;
            newList1.push(students[i].firstname);
          }
        }
        const formatedList1 = newList1.join(', ');
        console.log(`Number of students in ${field1}: ${counter1}. List: ${formatedList1}`);

        for (let i = 0; i < students.length; i += 1) {
          if (students[i].field === field2) {
            counter2 += 1;
            newList2.push(students[i].firstname);
          }
        }
        const formatedList2 = newList2.join(', ');
        console.log(`Number of students in ${field2}: ${counter2}. List: ${formatedList2}`);
      });
  }));
}

module.exports = countStudents;