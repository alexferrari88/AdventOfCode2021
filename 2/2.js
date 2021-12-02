const fs = require("fs");

function getData(file) {
  let rawData = fs.readFileSync(file, { encoding: "utf-8" });
  let data = rawData.trim().split("\n");
  data = data.map((el) => {
    tuple = el.split(" ");
    return [tuple[0].toLowerCase(), parseInt(tuple[1])];
  });
  return data;
}

function calculatePosition(data) {
  let [x, depth] = [0, 0];
  for (const tuple of data) {
    value = tuple[1];
    switch (tuple[0]) {
      case "forward":
        x += value;
        break;
      case "down":
        depth += value;
        break;
      case "up":
        depth -= value;
        break;
      default:
        break;
    }
  }
  return x * depth;
}

function calculatePositionWithAim(data) {
  let [x, depth, aim] = [0, 0, 0];
  for (const tuple of data) {
    value = tuple[1];
    switch (tuple[0]) {
      case "forward":
        x += value;
        depth += aim * value;
        break;
      case "down":
        // depth += value;
        aim += value;
        break;
      case "up":
        // depth -= value;
        aim -= value;
        break;
      default:
        break;
    }
  }
  return x * depth;
}

function main() {
  const data = getData("input.txt");
  const res1 = calculatePosition(data);
  const res2 = calculatePositionWithAim(data);
  console.log(`Part 1: ${res1}`);
  console.log(`Part 2: ${res2}`);
}

main();
