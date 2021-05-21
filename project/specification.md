# LaTTe
### A document system for humans
*I’m copying over some of the stuff from the old specification document, and rewriting some parts of it. Very much work in progress, and almost nothing other than math is implemented. — Tani*

## Project Overview

### Goals
*LaTTe*, pronounced like the coffee, is an easy-to-read, easy-to-write, and easy-to-extend way to create richly-formatted documents from plain text. It’s intended to be a superset of the Markdown language, but with a variety of new features.
It’s also intended to be highly modular — you should be able to drop in your own code, or write a new block, or add a new feature, with minimal effort.
The name is a pun on LaTeX, a document preparation system, but the goal is entirely different — you can start writing documents with relative ease, and get the rest figured out later. The mentality of this project is: “start with sensible defaults and change things if you want.”

### High Level Layout
There are a few major components to the LaTTe stack, explained by this handy diagram:

![Diagram of the LaTTe Stack](https://github.com/NotTani/LaTTe/blob/main/project/figure_1.png?raw=true)

## Specification
There are two modes in LaTTe: Document Mode and Embedded Mode. Document Mode is for complete documents written in LaTTe, generally with the .latte extension that are either supposed to be rendered into a PDF or full, optionally-styled, webpage. Embedded Mode is for partial documents, for example in a form field that allows for rich text. It will generate unstyled, basic HTML.

### The Document Header
Optionally, at the heading of any documents in Document Mode, you can specify a number of fields that a rendering engine can use to add into your document. The format for them is as follows:
```latte
---
Name: My First LaTTe Doc!
Author: Tani Nevins-Klein
Date: 5/24/2094
---
```

### Blocks
Blocks are essentially enclosing, nestable tags that change the way data in them is processed. Every syntactic element in LaTTe that encapsulates data in LaTTe is a Block underneath the surface. Every block has the default syntax of (italic means optional):

```latte
[<blocktype> <blockname>]
(<preference>, <value>; ...)
; Block body
[end <blockname>]
```


Custom blocks are encouraged to implement custom syntax to make them easier to learn. LaTTe comes with a number of blocks by default, covering many of the syntactic elements of Markdown, as well as a few of its own.
You can check out this list of built-in blocks, which I’m currently working on. This will change through the implementation phase, as I am able to figure out what to implement.

### Comments
Comments, unfortunately not inline with Python’s comments (due to the conflict with the header syntax), take more of a LISP route. They start with a semicolon, and end with a newline. Inline comments are not allowed to allow for semicolons within a paragraph. You can also escape semicolons with \;, but it's unlikely that you’ll need to.

```latte
; This is a comment, it will be ignored by the Parser
```

### Math
This is the old math specification (as I wrote it in previous years). I think it’s good enough for now, but once I start getting feedback on the specification, I may add new features or change existing ones.

There are a few elements to the Math language. It differs significantly from the rest of LaTTe. For the most part, it is similar to typical math syntax, with ^ for superscripts and |abs| for absolute value.

One extra concept is that of at (@) functions, which change the way things within them are displayed. They take the syntax of:

```
@function_name(parameter, parameter)[body_field]
```

Ideally @ functions are not needed for most common math syntax, and they exist as either an entry point to custom mathematical functions or to when the LaTTe engine can’t quite figure out what you mean. The exception is fractions, as it’s generally a bad behavior to assume when you want fractions and when you don’t.

```
; Math is enclosed in double
; curly braces. Add the d flag
; for nicer display on a single
; line
{{y = f(x)}}
; Superscripts are pretty simple:
{{3^2}}



; As are subscripts
{{3_n}}
; You can use a display function
; to do this as well
{{3@sub(n)}}

; Like square roots?
{{@sqrt(2)}}

; nRoots?
{{@root(2, 5)}}

; Fractions look like this
; Also note display mode
d{{@frac(1/2)}}

; They are also completely 
; nestable
{{@frac(1/@frac(1/3))}}

; Absolute value is also fairly
; simple, there are two ways:
{{|a|}}
; Or this
{{@abs(a)}}

; Sums are also pretty simple
d{@{sum(i=1, n)[2i]}}

; Infinite repeating decimals
d{{0.@overline(323)}}

; Limits
d{{@lim(a,b)f(x)}}

; Antiderivative
d{{@int()[f(x) dx]}}

; Integrals
d{{@int(a,b)[f(x) dx]}}

; Surface Integral
d{{@int(a,b,2)[f(x,y) dx dy]}}

; Closed-line integrals
d{{@intc(a,b)[f(x) dx]}}
```