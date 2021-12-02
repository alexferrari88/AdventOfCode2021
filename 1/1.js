const fs = require("fs");

function getData(file) {
  let rawData = fs.readFileSync(file, { encoding: "utf-8" });
  return rawData
    .trim()
    .split("\n")
    .map((el) => parseInt(el));
}

function countIncreases(data, windowSize = 1) {
  let [count, prevSum, currSum] = [0, 0, 0];
  for (let i = 0; i < windowSize; i++) {
    prevSum += data[i];
  }

  for (let i = 0; i < data.length - windowSize; i++) {
    currSum = prevSum - data[i] + data[i + windowSize];
    if (currSum > prevSum) count++;
    prevSum = currSum;
  }
  return count;
}

function main() {
  const data = getData("input.txt");
  let res1 = countIncreases(data);
  let res2 = countIncreases(data, 3);

  console.log(`Part 1: ${res1}`);
  console.log(`Part 2: ${res2}`);
}

main();
