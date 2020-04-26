package extractors

import (
	"log"
	"os"
	"path/filepath"
	"sync"

	"gitlab.com/rcmendes/go/find_duplicated_files/pkg/helpers"
	"gitlab.com/rcmendes/go/find_duplicated_files/pkg/metadata"
)

//GetFilesFromDir retrieves all files from an specific diretory and its subdirectories.
func GetFilesFromDir(rootDir string) (*metadata.ConcurrentFileMetaDataList, error) {
	files := metadata.NewConcurrentFileMetadataList()

	var wg sync.WaitGroup

	fileChannel := make(chan metadata.FileMetadata)

	go func() {
		isRunning := true
		for isRunning {
			select {
			case file, ok := <-fileChannel:
				if ok {
					files.Push(file)
				} else {
					isRunning = false
				}
			}
		}
	}()

	err := filepath.Walk(rootDir, func(path string, info os.FileInfo, err error) error {
		isDir, err := helpers.IsDirectory(path)
		if err != nil {
			log.Println("1")
			return err
		}

		if !isDir {
			wg.Add(1)
			go func(fileChannel chan<- metadata.FileMetadata) {
				file, err := metadata.NewFileMetadataFromFile(path)
				if err != nil {
					log.Printf("2:%s\n", path)
				}
				fileChannel <- *file
				wg.Done()
			}(fileChannel)
		}

		return nil
	})

	wg.Wait()

	close(fileChannel)

	return files, err
}
