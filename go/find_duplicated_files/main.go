package main

import (
	"flag"
	"fmt"
	"log"
	"os"

	"gitlab.com/rcmendes/go/find_duplicated_files/pkg/extractors"
)

func main() {
	var rootDir string
	flag.StringVar(&rootDir, "d", ".", "the root dir. e.g: -d=/home/files")

	// rootDir := "/Users/rodrigo/RcMendes80GoogleDrive/e-books"

	flag.Parse()

	info, err := os.Stat(rootDir)
	if err != nil {
		log.Fatal(err)
	}

	if !info.IsDir() {
		log.Fatalf("%s is not a directory\n", rootDir)
	}

	log.Printf("Find duplicated files in dir: %s\n", rootDir)

	duplicatedFilesMap, err := extractors.DuplicatedFilesFromDir(rootDir)
	if err != nil {
		log.Fatal(err)
	}

	for hash, files := range duplicatedFilesMap {
		fmt.Printf("> %s\n", hash)
		for _, file := range files.All() {
			fmt.Printf("\t- %s\n", file.String())
		}
	}

	log.Printf("Total of duplicated files found: %d", len(duplicatedFilesMap))

}
