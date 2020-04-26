package main

import (
	"fmt"
	"log"

	"gitlab.com/rcmendes/go/find_duplicated_files/pkg/extractors"
)

func main() {
	// rootDir := "/Users/rodrigo/git-projects"
	// rootDir := "/Users/rodrigo/Downloads"
	rootDir := "/Users/rodrigo/Downloads/assets"
	// rootDir := "/Users/rodrigo/RcMendes80GoogleDrive"

	files, err := extractors.GetFilesFromDir(rootDir)
	if err != nil {
		log.Fatal(err)
	}

	// for file := range files.Iterator() {
	// 	fmt.Printf("> %s\n", file.String())
	// }

	for _, file := range files.All() {
		fmt.Printf("> %s\n", file.String())
	}
}
