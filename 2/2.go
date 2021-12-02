package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type movement struct {
	direction string
	value     int
}

func getData(fileName string) []movement {
	rawByteData, err := ioutil.ReadFile(fileName)
	check(err)
	rawData := strings.TrimSpace(string(rawByteData))
	rawDataArray := strings.Split(rawData, "\n")
	data := make([]movement, len(rawDataArray))
	for i, v := range rawDataArray {
		tuple := strings.Split(v, " ")
		numericValue, err := strconv.Atoi(tuple[1])
		check(err)
		data[i] = movement{direction: tuple[0], value: numericValue}
	}
	return data
}

func calculatePosition(data []movement) int {
	var x, depth int
	for _, mov := range data {
		movValue := mov.value
		switch mov.direction {
		case "forward":
			x += movValue
		case "down":
			depth += movValue
		case "up":
			depth -= movValue
		}
	}
	return x * depth
}

func calculatePositionWithAim(data []movement) int {
	var x, depth, aim int
	for _, mov := range data {
		movValue := mov.value
		switch mov.direction {
		case "forward":
			x += movValue
			depth += aim * movValue
		case "down":
			aim += movValue
		case "up":
			aim -= movValue
		}
	}
	return x * depth
}

func main() {
	data := getData("input.txt")
	res1 := calculatePosition(data)
	res2 := calculatePositionWithAim(data)

	fmt.Println("Part 1: ", res1)
	fmt.Println("Part 2: ", res2)
}
