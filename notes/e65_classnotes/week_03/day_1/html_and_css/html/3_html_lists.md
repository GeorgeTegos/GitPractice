# HTML Lists

Let's dive into HTML lists. This is important because a lot of the data we display in web apps are lists. 

Even things that you wouldn't normally consider to be lists actually are. Consider a typical navigation header on a website. It's a 'list' of navigation items (e.g. Home, About, Contact).

Have a look at the [Gov.uk website](https://www.gov.uk/). How many lists can we see here? Most of the homepage is made up of lists! There's the 'Popular on GOV.UK' list of links, the navigation menu, the 'Topics', the 'Government activity', the 'Featured' etc. 

HTML provides three types of lists: unordered lists (`<ul>`), ordered lists (`<ol>`), and description lists (`<dl>` commonly used for glossaries or definitions.). We will mainly be focusing on `ul`. 

## Unordered Lists (`<ul>`):

Unordered lists are used to present items in a bulleted format. Each item is wrapped in a list item tag (`<li>`). 

Here's an example:

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

This will render as:

- Item 1
- Item 2
- Item 3

Often our `li` contains more than just text and we can use CSS (we'll get to that later) to remove the bullet points. Very useful!

Add the following code to your `index.html` document:

```html
<ul>
    <li>
        <div>
            <h3>Driving and Transport</h3>
            <p>Includes vehicle tax, MOT and driving licences</p>
        </div>
    </li>
    <li>
        <div>
            <h3>Driving and Transport</h3>
            <p>Includes vehicle tax, MOT and driving licences</p>
        </div>
    </li>
    <li>
        <div>
            <h3>Driving and Transport</h3>
            <p>Includes vehicle tax, MOT and driving licences</p>
        </div>
    </li>
</ul>

```

Here, the `li` tags contain `div` tags which in turn contain an `h3` and a `p`.


This will render as: 

<ul>
    <li>
        <div>
            <h3>Driving and Transport</h3>
            <p>Includes vehicle tax, MOT and driving licences</p>
        </div>
    </li>
    <li>
        <div>
            <h3>Driving and Transport</h3>
            <p>Includes vehicle tax, MOT and driving licences</p>
        </div>
    </li>
    <li>
        <div>
            <h3>Driving and Transport</h3>
            <p>Includes vehicle tax, MOT and driving licences</p>
        </div>
    </li>
</ul>

## Ordered lists

Try changing the `<ul>` in the above example to `<ol>`. The bullet points will turn into numbers. This is an ordered list.

## Navigation lists

Usually a navigation is made up of an unordered list. We 'wrap' the `ul` inside the `nav` tag. This won't display as you'd expect a navigation bar to display until we add CSS (more on that later). 

```html
<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/">News</a></li>
        <li><a href="/">Contact</a></li>
        <li><a href="/">About</a></li>
    </ul>
</nav>
```

### Further resources

- [The Description List element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
- [More on lists](https://www.w3schools.com/html/html_lists.asp)


# Next Lesson
[HTML Forms >>](./4_html_forms.md)