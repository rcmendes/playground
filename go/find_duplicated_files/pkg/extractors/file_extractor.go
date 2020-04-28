package extractors

import (
	"log"
	"os"
	"path/filepath"
	"sync"

	"gitlab.com/rcmendes/go/find_duplicated_files/pkg/helpers"
	. "gitlab.com/rcmendes/go/find_duplicated_files/pkg/metadata"
)

//GetFilesFromDirWithHash retrieves all files from an specific diretory and its subdirectories.
func GetFilesFromDirWithHash(rootDir string) (*ConcurrentFileMetaDataList, error) {
	files := NewConcurrentFileMetadataList()

	var wg sync.WaitGroup

	fileChannel := make(chan FileMetadata)

	go func() {
		for file := range fileChannel {
			files.Push(file)
		}
	}()

	err := filepath.Walk(rootDir, func(path string, info os.FileInfo, err error) error {
		isDir, err := helpers.IsDirectory(path)
		if err != nil {
			return err
		}

		if !isDir {
			wg.Add(1)
			go func(fileChannel chan<- FileMetadata) {
				defer wg.Done()
				file, err := NewFileMetadataFromFile(path)
				if err != nil {
					log.Fatal(err)
				}

				fileChannel <- *file
			}(fileChannel)
		}

		return nil
	})

	wg.Wait()

	close(fileChannel)

	return files, err
}

//GetFilesFromDir2 retrieves all files from an specific diretory and its subdirectories.
func groupFilesBySizeFromDir(rootDir string) (*ConcurrentFileMetadataMap, error) {
	filesBySize := NewConcurrentFileMetadataMap()

	var wg sync.WaitGroup

	fileChannel := make(chan FileMetadata)

	go func() {
		for file := range fileChannel {
			err := filesBySize.Append(file.Size(), file)
			if err != nil {
				log.Fatal(err)
			}
		}
	}()

	err := filepath.Walk(rootDir, func(path string, info os.FileInfo, err error) error {
		fileInfo, err := os.Stat(path)
		if err != nil {
			log.Printf("%s could not be handled. Error: %s", path, err.Error())
		} else if !fileInfo.IsDir() {
			wg.Add(1)
			go func(fileChannel chan<- FileMetadata) {
				defer wg.Done()
				file, err := NewFileMetadataFromFile(path)
				if err != nil {
					log.Println(err)
				} else {
					fileChannel <- *file
				}

			}(fileChannel)
		}

		return nil
	})

	wg.Wait()

	close(fileChannel)

	return filesBySize, err
}

func DuplicatedFilesFromDir(path string) (map[string]*ConcurrentFileMetaDataList, error) {
	duplicatedFileMap := make(map[string]*ConcurrentFileMetaDataList)

	filesBySize, err := groupFilesBySizeFromDir(path)
	if err != nil {
		log.Println("< 6 >")
		return nil, err
	}

	keySet := filesBySize.GetKeySet()
	for _, key := range keySet {
		files, ok := filesBySize.GetMetadataListByKey(key)

		if files.Length() > 1 {
			if ok {
				for _, file := range files.All() {
					hash, err := file.Hash()
					if err != nil {
						log.Println("< 7 >")
						return nil, err
					}
					list, ok := duplicatedFileMap[hash]
					if !ok {
						list = NewConcurrentFileMetadataList()
					}

					list.Push(file)
					duplicatedFileMap[hash] = list

				}
			}
		}
	}

	return duplicatedFileMap, nil
}
