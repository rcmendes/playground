package com.example.duplicated_files

import java.io.File
import java.security.MessageDigest
import java.util.*
import kotlin.collections.HashMap
import kotlin.collections.HashSet

fun main() {
//    val rootDir = "/Users/rodrigo/Downloads"
    val rootDir ="/Users/rodrigo/RcMendes80GoogleDrive/e-books"
    val result       = getDuplicatedFilesFromDir(rootDir)
    for ((hash, files) in result) {
        println("$hash:")
        files.forEach {
            println("\t$it")
        }
    }

}

fun getDuplicatedFilesFromDir(path: String): FilesByHash {
    val files = getFilesFromDir(path)
    val groupByLength = groupFilesByLength(files)
    val groupByHash = groupFilesByHash(groupByLength)
    return filterByGroupSize(filesByHash = groupByHash)
}

fun getFilesFromDir(path: String, minimumLength: Long = 1): FileList {
    val dir = File(path)
    if (!dir.isDirectory) {
        throw IllegalArgumentException("Path $path is not a directory")
    }

    val files = FileList()

    dir.walk().forEach {
        if (it.isFile && it.length() >= minimumLength && it.name != ".DS_Store") {
            files.add(FileInfo(path = it.path, length = it.length()))
        }
    }

    return files
}

fun filterByGroupSize(filesByHash: FilesByHash, minimum: Int = 2): FilesByHash {
    val filteredData = FilesByHash()
    for ((hash, files) in filesByHash) {
        if (files.size >= minimum) {
            filteredData[hash] = files
        }
    }

    return filteredData
}

fun groupFilesByHash(filesByLength: FilesByLength): FilesByHash {
    val filesByHash = FilesByHash()

    for ((_, files) in filesByLength) {
        files.forEach { file ->
            val hash = calculateHash(File(file.path))
            val list = filesByHash.getOrDefault(hash, FileList())
            list.add(file)
            filesByHash[hash] = list
        }
    }

    return filesByHash
}

fun groupFilesByLength(files: FileList): FilesByLength {
    val filesByLength = FilesByLength()

    files.forEach { fileInfo ->
        val length = fileInfo.length
        val list = filesByLength.getOrDefault(length, FileList())
        list.add(fileInfo)
        filesByLength[length] = list
    }

    return filesByLength
}


fun calculateHash(file: File): String {
    val content = file.readBytes()
    val algorithm = MessageDigest.getInstance("SHA-256")
    val data = algorithm.digest(content)
    val base64 = Base64.getEncoder()
    return base64.encodeToString(data)
}

data class FileInfo(val path: String, val length: Long)

typealias FileList = HashSet<FileInfo>
typealias FilesByLength = HashMap<Long, FileList>
typealias FilesByHash = HashMap<String, FileList>