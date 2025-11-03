from inspect import signature, getdoc
from fastmcp import FastMCP

print(signature(FastMCP))           # shows accepted kwargs
print(getdoc(FastMCP.__init__))     # any docstring hints