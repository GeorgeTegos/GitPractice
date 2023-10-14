# HTML Elements 

HTML tags (formally known as HTML elements) are usually nested inside each other to create the desired structure.

## Nesting tags

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My HTML document</title>
  </head>
  <body>
    <h1>Welcome to my HTML document</h1>
  </body>
</html>
```

In the above example the `h1` tag is nested inside the `body` tag. 

## Top 10 Commonly used HTML elements 

- `<h1>` to `<h6>` Heading tags used to define different levels of headings, with `<h1>` being the highest level and `<h6>` the lowest. (Your document should have only one `h1` tag) 
- `<p>` Represents a paragraph of text.
- `<a>` Creates a hyperlink, allowing you to link to other web pages or resources.
- `<img>` Inserts an image into the webpage, with attributes like src (source) and alt (alternative text).
- `<ul>` and `<li>` Used together to create an unordered (bulleted) list, with `<ul>` as the container and `<li>` for each list item.
- `<div>` A generic container that helps group and style other elements together. It's commonly used for layout purposes.
- `<span>` Inline container for styling specific portions of text.
- `<input>` Creates form input fields for user input.
- `<button>` Represents a clickable button.
- `<table>`, `<tr>`, `<td>` Used together to create tables with rows and cells.


Add the following code to your `index.html` between the opening and closing `body` tags:

```html
  <!-- ... as before  -->
  <div>
    <h1>Welcome to my HTML document</h1>
    <h2>Heading 2</h2>
    
    <p>This is a paragraph of text.</p>
    
    <a href="https://www.example.com">Visit Example.com</a>
    
    <img src="https://picsum.photos/200/300" alt="Random Image">
    
    <ul>
      <li>List item 1</li>
      <li>List item 2</li>
      <li>List item 3</li>
    </ul>
    
    <p>This is a <span>span element</span> within a paragraph.</p>
    
    <input type="text" placeholder="Enter your name">
    
    <button>Click me</button>
    
    <table>
      <tr>
        <td>Table cell 1</td>
        <td>Table cell 2</td>
      </tr>
      <tr>
        <td>Table cell 3</td>
        <td>Table cell 4</td>
      </tr>
    </table>
  </div>
```

## Attributes

HTML element attributes provide additional information about an HTML element and modify its behaviour or appearance. Attributes are added to HTML tags and are defined within the opening tag using name-value pairs. Here are some key points about HTML element attributes:

1. Syntax: Attributes are written in the format `name="value"`, where `name` is the attribute name, and `value` is the attribute value enclosed in quotes.

2. Common Attributes: Some commonly used attributes include `class, id, style, src, href, alt`. These attributes allow you to specify CSS classes, unique identifiers, inline styles, image sources, link destinations, and alternative text, respectively.

3. Accessibility Attributes: HTML5 introduced a set of attributes to enhance web accessibility, such as `aria-label`, `aria-labelledby`, and `role`. These attributes provide information to assistive technologies and improve the accessibility of your web content.

In the above example, the `<a>` tag has an `href` (link destination) attribute. What other attributes can you spot in the above example? 

#### Answer

- The `img` tag has a `src` attribute
- The `input` tag has `type` and `placeholder` attributes 

## Accessibility

Accessibility is the practice of making your websites usable by as many people as possible. We traditionally think of this as being about people with disabilities, but the practice of making sites accessible also benefits other groups such as those using mobile devices, or those with slow network connections.

WAI-ARIA (Web Accessibility Initiative - Accessible Rich Internet Applications) is a specification written by the W3C, defining a set of additional HTML attributes that can be applied to elements to provide additional semantics and improve accessibility wherever it is lacking.

[Read more about accessibility](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)

## Classes & ids

Two of the important attributes you'll use are `class` and `id`. These are primarily used to allow a CSS rule to be applied to the element.


## HTML validation tool

It's important that we format our HTML correctly so that all browsers can read them correctly. It's also important that we try to follow the `Web Content Accessibility Guidelines (WCAG)` and vaildators can help us spot our errors. 

Finally, search engines rely on well-structured and valid HTML to understand and index web pages effectively.

Try copying and pasting your HTML into the [W3 (The World Wide Web Consortium) validator](https://validator.w3.org/#validate_by_input) and see what results you get.


# Next Lesson
[HTML Lists >>](./3_html_lists.md)