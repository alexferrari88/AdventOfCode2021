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

func countIncreases(data []int, windowSize int) (count int) {
	if windowSize == 0 {
		windowSize = 1
	}
	dataSize := len(data)
	var currWindowSum, prevWindowSum int
	for _, val := range data[:windowSize] {
		prevWindowSum += val
	}

	for i := 0; i < dataSize-windowSize; i++ {
		currWindowSum = prevWindowSum - data[i] + data[i+windowSize]
		if currWindowSum > prevWindowSum {
			count++
		}
		prevWindowSum = currWindowSum
	}

	return

}

func getData(file string) []int {
	rawData, err := ioutil.ReadFile(file)
	check(err)
	rawDataSlice := strings.Split(string(rawData), "\n")
	data := make([]int, len(rawDataSlice))

	for i := 0; i < len(rawDataSlice); i++ {
		data[i], _ = strconv.Atoi(rawDataSlice[i])
	}
	return data
}

func main() {
	data := getData("input.txt")
	res1 := countIncreases(data, 1)
	res2 := countIncreases(data, 3)

	fmt.Println("Part 1:", res1)
	fmt.Println("Part 2:", res2)
}
