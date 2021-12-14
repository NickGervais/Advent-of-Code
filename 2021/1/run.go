package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	// open file
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	// remember to close the file at the end of the program
	defer f.Close()

	var depths []int
	// read the file line by line using scanner
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		intVar, _ := strconv.Atoi(scanner.Text())
		depths = append(depths, intVar)
	}

	var sections []int
	for i := 0; i < len(depths)-2; i++ {
		section := 0
		for _, num := range depths[i : i+3] {
			section += num
		}
		sections = append(sections, section)
	}

	level_1_total_increases := 0
	for i, depth := range depths {
		if i != 0 {
			if depth > depths[i-1] {
				level_1_total_increases++
			}
		}
	}

	level_2_total_increases := 0
	for i, section := range sections {
		if i != 0 {
			if section > sections[i-1] {
				level_2_total_increases++
			}
		}
	}

	fmt.Println(level_1_total_increases)
	fmt.Println(level_2_total_increases)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
