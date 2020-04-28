package metadata

import (
	"sync"
)

// ConcurrentFileMetaDataList manages a list of FileMetadata entities in a thread-safe way.
type ConcurrentFileMetaDataList struct {
	sync.RWMutex
	files []*FileMetadata
}

//NewConcurrentFileMetadataList creates a instance of a ConcurrentFileMetaDataList.
func NewConcurrentFileMetadataList() *ConcurrentFileMetaDataList {
	return &ConcurrentFileMetaDataList{
		files: make([]*FileMetadata, 0),
	}
}

//Push adds a FileMetadata entity into the list.
func (list *ConcurrentFileMetaDataList) Push(file FileMetadata) {
	list.RLock()
	defer list.RUnlock()

	list.files = append(list.files, &file)
}

//All lists all FileMetadata entities from the list.
func (list *ConcurrentFileMetaDataList) All() []FileMetadata {
	responseList := make([]FileMetadata, 0, len(list.files))
	list.Lock()
	defer list.Unlock()

	for _, file := range list.files {
		responseList = append(responseList, *file)
	}

	return responseList
}

//Length informs the number of elements stored into the list.
func (list *ConcurrentFileMetaDataList) Length() int {
	return len(list.files)
}

//Iterator provides an iterator channell to read all FileMetadata entities from the list.
func (list *ConcurrentFileMetaDataList) Iterator() <-chan *FileMetadata {
	fileChannel := make(chan *FileMetadata)

	go func() {
		list.Lock()
		defer list.Unlock()

		for _, file := range list.files {
			fileChannel <- file
		}

		close(fileChannel)
	}()

	return fileChannel

}
