package metadata

import (
	"fmt"
	"sync"
)

type concurrentMap = map[interface{}]*ConcurrentFileMetaDataList

// ConcurrentFileMetadataMap manages a list of FileMetadata entities in a thread-safe way.
type ConcurrentFileMetadataMap struct {
	sync.RWMutex
	filesByKey concurrentMap
}

//NewConcurrentFileMetadataMap creates a instance of a ConcurrentFileMetadataMap
func NewConcurrentFileMetadataMap() *ConcurrentFileMetadataMap {
	return &ConcurrentFileMetadataMap{
		filesByKey: make(concurrentMap),
	}
}

func (mapper *ConcurrentFileMetadataMap) Append(key interface{}, file FileMetadata) error {
	mapper.RLock()
	defer mapper.RUnlock()

	if key == nil {
		return fmt.Errorf("Key cannot be nil")
	}

	files, ok := mapper.filesByKey[key]
	if !ok {
		files = NewConcurrentFileMetadataList()
	}

	files.Push(file)
	mapper.filesByKey[key] = files

	return nil
}

func (mapper *ConcurrentFileMetadataMap) GetMetadataListByKey(key interface{}) (*ConcurrentFileMetaDataList, bool) {
	mapper.Lock()
	defer mapper.Unlock()
	files, ok := mapper.filesByKey[key]
	return files, ok
}

func (mapper *ConcurrentFileMetadataMap) GetKeySet() []interface{} {
	mapper.Lock()
	defer mapper.Unlock()

	keySet := make([]interface{}, 0, len(mapper.filesByKey))

	for key := range mapper.filesByKey {
		keySet = append(keySet, key)
	}

	return keySet
}

func (mapper *ConcurrentFileMetadataMap) GetMap() map[interface{}]*ConcurrentFileMetaDataList {
	return mapper.filesByKey
}
