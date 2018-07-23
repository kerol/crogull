macro_rules! expect_char {
    ($iter:expr, $ch:expr) => (
        while $iter.next() != Some(&$ch) {}
    )
}

fn main() {
    let bts = b"GET /?foo=bar HTTP/1.1\r\ncache-control: no-cache\r\nPostman-Token: 6ce8ed27-8207-4d9a-9b85-7989e7dca790\r\nUser-Agent: PostmanRuntime/7.1.5\r\nAccept: */*\r\nHost: 127.0.0.1:8000\r\naccept-encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n";
    rs_parse_request(bts);
}

// get, post, put, delete, head, connect, options, patch
fn rs_parse_request(bts: &[u8]) {
    println!("{}", "rust parse http request");
    let mut iter = bts.iter();
    let mut method = "".to_string();
    let mut ch = iter.next();
    assert!(ch.is_ascii());
    while ch != Some(&b' ') {
        method.push_str(&ch);
    }
    println!("{}", method);
    if ch == Some(&b'G') {
        println!("GET");
    }
    else if ch == Some(&b'P') {
        println!("POST");
    }
    else {
        println!("Error");
    }
    expect_char!(iter, b' ');
    ch = iter.next();
    if ch == Some(&b'/') {
        println!("GGG");
    }
}