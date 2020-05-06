use std::io::prelude::*;
// use std::io::BufReader;
use std::net::{TcpListener, TcpStream};
use std::thread;

fn main() {
    let listener =
        TcpListener::bind("127.0.0.1:5001").expect("Fail to listen port 5000 on localhost");

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        thread::spawn(move || {
            handle_stream(stream).expect("Fail on handling stream.");
        });
    }
}

fn handle_stream(mut stream: TcpStream) -> std::io::Result<()> {
    let mut buffer = [0; 512];

    let mut data = String::from("");

    loop {
        let bytes_read = stream.read(&mut buffer)?;
        data.push_str(&String::from_utf8_lossy(&buffer[0..bytes_read]));
        if bytes_read < buffer.len() {
            break;
        }
    }

    write_response(&mut stream)?;

    println!("Bytes read: {}", data.len());

    let lines = data.split("\n");
    for line in lines {
        println!("{}", line);
    }

    Ok(())
}

fn write_response(stream: &mut TcpStream) -> std::io::Result<()> {
    let response_status = String::from("HTTP/1.1 OK 200\r\n");
    stream.write(response_status.as_bytes())?;

    let body = b"Request received!";
    stream.write(&format!("Content-Length: {}\r\n\r\n", body.len()).as_bytes())?;
    stream.write(body)?;

    stream.flush()?;
    Ok(())
}
