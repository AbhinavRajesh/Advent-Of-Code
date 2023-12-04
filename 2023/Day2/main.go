package main

import (
	"fmt"
	"strings"
	"os"
	"log"
	"bufio"
	"strconv"
)

func part1() {
	file, err := os.Open("input.txt")

    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

	scanner := bufio.NewScanner(file)

	limits := map[string]int {
		"red": 12,
		"green": 13,
		"blue": 14}

	sum1 := 0
	
    for scanner.Scan() {
        text := scanner.Text()

		g := strings.Split(text, ":")
		gameId, err1 := strconv.Atoi(strings.Split(g[0], " ")[1])

		games := strings.Split(g[1], ";")

		flag := false

		for _, game := range games {
			balls := strings.Split(game, ",")
			for _, ball := range balls {
				sball := strings.Split(ball, " ")


				numberOfBalls, ballErr :=  strconv.Atoi(sball[1])

				if ballErr != nil {
					fmt.Println(ballErr)
				}
				
				if limits[sball[2]] < numberOfBalls {
					flag = true
					break
				}
			}
			if flag {
				break
			}
		}
		
		if !flag {
			sum1 += gameId
		}

		if err1 != nil {
			fmt.Println(err)
		}

	}

	fmt.Println("Part 1: ", sum1)
}

func part2() {
	file, err := os.Open("input.txt")

	if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

	scanner := bufio.NewScanner(file)
	sum := 0
	
    for scanner.Scan() {
        text := scanner.Text()

		limits := map[string]int {
			"red": 0,
			"green": 0,
			"blue": 0}

		g := strings.Split(text, ":")

		games := strings.Split(g[1], ";")

		for _, game := range games {
			balls := strings.Split(game, ",")
			for _, ball := range balls {
				sball := strings.Split(ball, " ")
				numberOfBalls, ballErr :=  strconv.Atoi(sball[1])

				if ballErr != nil {
					fmt.Println(ballErr)
				}
				
				if limits[sball[2]] < numberOfBalls {
					limits[sball[2]] = numberOfBalls
				}
			}
		}

		power := limits["red"] * limits["green"] * limits["blue"]
		sum += power

	}

	fmt.Println("Part 2: ", sum)
}

func main() {
	part1()
	part2()

    
}