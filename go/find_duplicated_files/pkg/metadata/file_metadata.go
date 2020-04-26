package metadata

import (
	"fmt"
	"os"

	"gitlab.com/rcmendes/go/find_duplicated_files/pkg/helpers"
)

//FileMetadata provides information about an specific file.
type FileMetadata struct {
	path string
	size uint64
	hash string
}

func (meta *FileMetadata) String() string {
	size := meta.size / 1024
	return fmt.Sprintf("%s | %d kb | {%s}", meta.path, size, meta.hash)
}

//Path defines the path of the file.
func (meta *FileMetadata) Path() string {
	return meta.path
}

//Size defines the size, in bytes, of the file.
func (meta *FileMetadata) Size() uint64 {
	return meta.size
}

//Hash defines the hash of the file data.
func (meta *FileMetadata) Hash() string {
	return meta.hash
}

//NewFileMetadataFromFile create a FileMetadata of the file.
func NewFileMetadataFromFile(filePath string) (*FileMetadata, error) {
	fileInfo, err := os.Stat(filePath)
	if err != nil {
		return nil, err
	}

	if fileInfo.IsDir() {
		return nil, fmt.Errorf("%s is a diretory", filePath)
	}

	hash, err := helpers.CalculateFileHash(filePath)
	if err != nil {
		return nil, err
	}

	return &FileMetadata{path: filePath, size: uint64(fileInfo.Size()), hash: hash}, nil
}
