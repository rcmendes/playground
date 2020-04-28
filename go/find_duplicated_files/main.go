package main

import (
	"fmt"
	"log"

	"gitlab.com/rcmendes/go/find_duplicated_files/pkg/extractors"
)

func main() {
	// rootDir := "/Users/rodrigo/git-projects"
	// rootDir := "/Users/rodrigo/Downloads"
	// rootDir := "/Users/rodrigo/Downloads/assets"
	rootDir := "/Users/rodrigo/RcMendes80GoogleDrive/e-books"

	// files, err := extractors.GetFilesFromDirWithHash(rootDir)
	// for _, file := range files.All() {
	// 	fmt.Printf("> %s\n", file.String())
	// }

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

}
