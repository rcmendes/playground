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
	hash *string
}

func (meta *FileMetadata) String() string {
	size := meta.size / 1024

	if meta.hash == nil {
		return fmt.Sprintf("%s | %d kb", meta.path, size)
	}

	return fmt.Sprintf("%s | %d kb | {%v}", meta.path, size, meta.hash)
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
func (meta *FileMetadata) Hash() (string, error) {
	if meta.hash == nil {
		hash, err := helpers.CalculateFileHash(meta.path)
		if err != nil {
			return "", err
		}
		meta.hash = &hash
	}
	return *meta.hash, nil
}

//NewFileMetadataFromFile create a FileMetadata of the file.
func NewFileMetadataFromFile(path string) (*FileMetadata, error) {
	fileInfo, err := os.Stat(path)
	if err != nil {
		return nil, err
	}

	if !fileInfo.Mode().IsRegular() {
		return nil, fmt.Errorf("%s is not a file", path)
	}

	return &FileMetadata{path: path, size: uint64(fileInfo.Size()), hash: nil}, nil
}
