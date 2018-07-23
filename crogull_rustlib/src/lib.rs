#![feature(proc_macro, specialization)]

extern crate pyo3;
use pyo3::prelude::*;

use pyo3::py::modinit as pymodinit;

/// This module is implemented in Rust.
#[pymodinit(crogull_rust)]
fn init_mod(py: Python, m: &PyModule) -> PyResult<()> {

    #[pyfn(m, "sum_as_string")]
    fn sum_as_string_py(a: i64, b: i64) -> PyResult<String> {
       Ok(sum_as_string(a, b))
    }

    #[pyfn(m, "parser_header")]
    fn parser_header_py(h: String) -> PyResult<String> {
        Ok(parser_header(h))
    }

    Ok(())
}

// test func
fn sum_as_string(a: i64, b: i64) -> String {
    format!("{}", a + b).to_string()
}

// parse header
fn parser_header(h: String) -> String {
    return "parserlib header".to_string()
}
