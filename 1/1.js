const fs = require("fs");

function solvePart1(data) {
  let count = 0;

  for (let i = 1; i < data.length; i++) {
    if (data[i] > data[i - 1]) {
      count++;
    }
  }

  return count;
}

function solvePart2(data) {
  const k = 3;
  let currSum = 0;
  let prevSum = 0;
  let count = 0;

  for (let i = 0; i < k; i++) {
    prevSum += data[i];
  }

  for (let i = 0; i < data.length - k; i++) {
    currSum = prevSum - data[i] + data[i + k];
    if (currSum > prevSum) count++;
    prevSum = currSum;
  }
  return count;
}

fs.readFile("1_input.txt", "utf-8", (err, rawData) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = rawData
    .trim()
    .split("\n")
    .map((el) => parseInt(el));

  console.log(`Part 1: ${solvePart1(data)}`);
  console.log(`Part 2: ${solvePart2(data)}`);
});
