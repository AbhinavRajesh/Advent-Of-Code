package main

import (
	"fmt"
	"os"
	"log"
	"bufio"
	"regexp"
	"strconv"
	"strings"
)

func getFirstAndLastFromList(str string, elements []string) []string {
	strLen := len(str)
	
	var s []string

	flag := false
	// Get first match from front of string
	for i := 0; i < len(str); i++ {
		for _, element := range elements {
			if strings.HasPrefix(str[i:strLen], element) {
				s = append(s, element)
				flag = true
				break
			}
		}
		if flag {
			break
		}
	}
	
	flag = false
	
	// Get first match from front of string
	for i := len(str) - 1; i >= 0 ; i-- {
		for _, element := range elements {
			if strings.HasPrefix(str[i:strLen], element) {
				s = append(s, element)
				flag = true
				break
			}
		}
		if flag {
			break
		}
	}

	return s
}

func main() {
	file, err := os.Open("input.txt")

    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)

	numbersSpelled := map[string]string {
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five": "5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9"}

	keys := make([]string, len(numbersSpelled))

	i := 0
	for k := range numbersSpelled {
	  keys[i] = k
	  i++
	}

	sum1 := 0
	sum2 := 0

	elements1 := []string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
	elements2 := append(keys, elements1...)
	
    for scanner.Scan() {
        text := scanner.Text()

		part1Strings := getFirstAndLastFromList(text, elements1)

		number1, err1 := strconv.Atoi(part1Strings[0] + part1Strings[1])
		
		sum1 += number1

		if err1 != nil {
			fmt.Println(err)
		}

		numberS := ""

		part2Strings := getFirstAndLastFromList(text, elements2)

		numberRegex := regexp.MustCompile(`\d`)
		
		for _, numS := range part2Strings {
			if numberRegex.MatchString(numS) {
				numberS += numS
			} else {
				numberS += numbersSpelled[numS]
			}
		}
		
		number2, err2 := strconv.Atoi(numberS)

		if err2 != nil {
			fmt.Println(err)
		}
		
		sum2 += number2
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

	fmt.Println("Part 1: ", sum1)
	fmt.Println("Part 2: ", sum2)
}