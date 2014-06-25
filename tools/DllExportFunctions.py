#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Step 1. Check file type
# Step 2. Check PE Header
# Step 3. Find magic word byte of '0x10b' => '0b01', means PE32 header
# Step 4. From the magic word shift 96 bytes to get export table base address
#         and export table size
#         export table base address => 4 bytes
#         export table size         => 4 bytes
#         Example: a006 0100 c103 0000
#                  => 0001a006 (export table base address)
#                  => 000003c1 (export table size)
# Step 5. Jump to export table base address and read size of export table
# Step 6. First 40 bytes has a specific struct to read it
# struct {
#        DWORD  export_flasg;   // Must be 0x00000000                   0  ~  3
#        DWORD  time;           // Timestamp of export table created    4  ~  7
#        WORD   major_version;  // Version number user defined          8  ~  9
#        WORD   minor_version;  // Version number user defined          10 ~ 11
#        DWORD  name;           // Name of dll RVA                      12 ~ 15
#        DWORD  obase;          // Start number of ordinal table        16 ~ 19
#        DWORD  entries;        // Number of entries in addr table      20 ~ 23
#        DWORD  numofbptrs;     // Number of entries in nptr table      24 ~ 27
#        DWORD  addrtable;      // Address of export addr table RVA     28 ~ 31
#        DWORD  nptrtable;      // Address of export nptr table RVA     32 ~ 35
#        DWORD  otable;         // Address of ordinal table RVA         36 ~ 40
# }
# Step 7. Read name pointer table to get function names

import sys


def reversehex2number(s):
    """Return dec number from reversed hex string"""
    return int(s[-1::-1].encode('hex'), 16)


def findbaseptraddrsize(data, cursor=0):
    """Find export function table base pointer and table size and return"""
    while True:
        if data[cursor] == '\x0b':
            if data[cursor + 1] == '\x01':
                break
        cursor += 1
    cursor += 96
    bptr = reversehex2number(data[cursor:cursor+4])
    size = reversehex2number(data[cursor+4:cursor+8])
    return bptr, size


def exportfunctionnames(data, bptr, size):
    """return names of export functions"""
    tables = data[bptr:bptr+size]
    if tables[0:4] != '\x00\x00\x00\x00':
        return None
    entries = reversehex2number(tables[20:24])
    nptr = reversehex2number(tables[32:36]) - bptr
    names = []
    cur = nptr
    for i in range(entries):
        np = reversehex2number(tables[cur:cur+4]) - bptr
        name = ''
        while True:
            if tables[np] == '\x00':
                break
            name += tables[np]
            np += 1
        cur += 4
        names.append(name)
    return names


def test(fname):
    with open(fname, 'r') as fin:
        data = fin.read()
    bptr, size = findbaseptraddrsize(data)
    names = exportfunctionnames(data, bptr, size)
    return names


if __name__ == '__main__':
    print sys.argv[1]
    names = test(sys.argv[1])
    print names
