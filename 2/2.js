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
  let x = (depth = 0);
  for (const tuple of data) {
    switch (tuple[0]) {
      case "forward":
        x += tuple[1];
        break;
      case "down":
        depth += tuple[1];
        break;
      case "up":
        depth -= tuple[1];
      default:
        break;
    }
  }
  return x * depth;
}

function main() {
  const data = getData("input.txt");
  const res1 = calculatePosition(data);
  console.log(res1);
}

main();
