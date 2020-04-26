package helpers

import (
	"crypto/md5"
	"encoding/hex"
	"io"
	"os"
)

// IsDirectory verifies if a path refers to an directory or a file.
func IsDirectory(path string) (bool, error) {
	fileInfo, err := os.Stat(path)
	if err != nil {
		return false, err
	}
	return fileInfo.IsDir(), err
}

//CalculateFileHash calculas a hash of a file
func CalculateFileHash(filePath string) (string, error) {
	f, err := os.Open(filePath)
	defer f.Close()

	if err != nil {
		return "", err
	}

	hash := md5.New()
	if _, err := io.Copy(hash, f); err != nil {
		return "", err
	}

	return hex.EncodeToString(hash.Sum(nil)), nil

}
