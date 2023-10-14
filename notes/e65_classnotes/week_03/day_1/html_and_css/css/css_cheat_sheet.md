# CSS Cheat Sheet

CSS (Cascading Style Sheets) is a language that is used in combination with HTML to customise how HTML elements will appear. CSS can define styles and change the layout and design of a document.

## Linking CSS to HTML

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

In the example above, the `<link>` element is placed within the `<head>` section. The rel attribute specifies the relationship between the HTML document and the linked file, and the href attribute specifies the path or URL to the stylesheet file. In this case, the stylesheet file is named `style.css` and is located in the same directory as the HTML file.

## Style Rules & Terminology

```css
.welcome-text {
  color: green;
  margin-top: 24px;
}
```

This whole things is called a `rule`

`.welcome-text` is called the `selector`

`color` is called a `property`

`color: green;` is called a `declaration`

`24px` is called a `unit`

## Selectors

### Element Selectors

```css
/* Make all h1 elements black */
h1 {
    color: black;
}

/* Remove the underscore from all anchor tags */

a {
    text-decoration: none;
}
```

### Class Selectors

```css
/* Give all the elements with class 'card' a top margin */

.card {
    top-margin: 10px;
}
```

### ID Selectors

```css
/* Give the element with id 'main-section' a flex display */

#main-section {
    display: flex;
}
```

## Pseudo-classes

```css
/* :hover is one of the most common pseudo-classes */
/* Remove the underscore from all links on hover */

a:hover {
    text-decoration: none;
}
```

## Combinators

Combinators are characters between selectors that combine elements

### The space combinator (all descendants!)

Add a space between 'nav' and 'a'

```css
/* Make all links inside a nav blue and bold */
/* This applies to all links no matter how deeply nested they are within the nav */

nav a {
  color: blue;
  font-weight: bold;
}

/* Target ONLY the direct children */

nav > a {
  color: blue;
  font-weight: bold;
}
```

## Color

We can target the text color of an element.

```css
/* Make all h1 text red */

h1 {
    color: red
}

/* Make the background color of all h1 black */
h1 {
    background-color: red;
}
```

There are 4 main ways to represent color.

1. We can use the word like 'red' or 'dodgerblue'
2. Hex codes (#FF0000)
3. rgb(255, 0, 0)
4. hsl(100deg, 100%, 50%)

We don't want to use the words like 'red' because it's not specific enough.
Hex codes are common. The first 2 figures represent red, the second 2 green and the third 2 blue. There are 16 possibilities for each. But it's quite confusing and not easy to read and parse.  
`rgb` stands for red, green blue and works the same as hex but using decimal.

HSL is recommended. It's easy to see how you can adjust it straight in VSCode without needing a color picker. The first value is the hue and is represented as degrees. The second is saturation and the third is lightness.

https://www.w3schools.com/colors/colors_hsl.asp

## Units

Pixels are the most common unit.

```css
.card {
    padding: 10px;
    margin-top: 12px;
    width: 100px;
}
```

Pixels are fine for most things EXCEPT typography.

### ems

ems are a relative unit, equal to the font size of the current element.

If a paragraph has a font-size of 12px, and we give it a bottom padding of 2em, we can expect that the element will have 24px of padding underneath it (2 × 12px)

### rems

rems are better because it's always relative to the root HTML element which browsers will default to 16px. This makes it more predictable and consistent throughout the DOM tree. For example:

```css
/* Make all paragraph text 16px */
p {
    font-size: 1rem;
}


/* Make all h1 text 32px */
h1 {
    font-size: 2rem;
}
```

### Percentages

Percentages can be used to make a child element relative in size to it's parent.

```css
/* Make the inner card 50% of the width and height of it's parent, the .card */

.card {
    width: 250px;
    height: 250px;
}

.inner-card{
    width: 50%;
    height: 50%;
}

```

### Which units to use?

- For typography use rem, because it has important accessibility benefits. (people might adjust their default font size)
- For properties that relate to the box model — padding, border, margin —  use pixels.
- For width/height use pixels or percentages.

## Typography

To define the font we use font-family. It's a family because it's made up of multiple character sets. "Roboto" includes 12 sets, 6 font weights and normal/italic.

```css
body{
    font-family: Roboto;
}
```

We can let the operating system choose a relevant font. Serif, sans-serif or monospace. Sans-serif is most common on the web. Serif will give the font a more classical feel.

```css
body {
    font-family: sans-serif;
}
```

We can also import custom fonts such as Google fonts.


```html
<!-- Make Montserrat weight 100 available -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100&display=swap" rel="stylesheet">
```

### Font weight

```css
/* thin */
font-weight: 300;

/* normal (the default) */
font-weight: 400;

/* bold */
font-weight: 700;

/* or */
font-weight: bold;

```

Using a `<strong>` tag will also make text bold but it also has semantic meaning. It stresses that it's important.

### Italics

```css
font-style: italic;
```

### Underlined text

```css
/* Remove underlines from all links */

a{
    text-decoration: none;
}

/* Add an underline to all links (default) */

a{
    text-decoration: underline;
}
```

### Aligning text

```html
<p class="left">
  This paragraph uses the default “left” alignment.
</p>
<p class="right">
  This one, meanwhile, pops over to the other side! It flips the default behaviour.
</p>
<p class="center">
  Finally, we end in the middle.
</p>
```

```css
p.left {
  text-align: left;
}
p.right {
  text-align: right;
}
p.center {
  text-align: center;
}

```

### Text transforms

```css
/* ALL CAPS */
text-transform: uppercase;

/* Capitalize The First Letter Of Every Word */
text-transform: capitalize;
```

### Spacing

letter-spacing is horizontal, line-height is vertical. Line-height works as a ratio. Recommended value is 1.5 for accesssibility and readability.

```css
h3 {
  letter-spacing: 32px;
  line-height: 5;
}
```

## Flex Layout

The default flow layout is great for the original purpose of HTML & CSS - namely laying documents out a bit like a newspaper. 

However, as the web has developed, user interfaces have become increasingly complex. Probably the best and easiest approach to layout is the `flex layout` (A.K.A Flexbox).

For a good understanding of Flexbox, checkout the first half of [this interactive guide](https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/) (up to but not including "Hypothetical size")

## Debugging with Chrome devtools

Right click on the browser ans select "Inspect". Open the "Elements" tab and the "Styles" tab.

Here you can see the CSS that is applied to the HTML elements. You can edit your CSS here and see it change in the browser.

Remember though that any changes you make in the Devtools will need to be copied into your actual CSS file otherwise they won't be saved.