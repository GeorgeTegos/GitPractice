# CSS Layout

## Getting things in the right place

This is one of the hardest things in CSS so let's quickly cover a **little** bit of theory.

## Flow Layout

CSS has 7 distinct layout modes. You will already have heard of some of them. Like Flexbox (technically flexible box layout) and Grid.

https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_mode

The default is "Normal Flow" aka Flow Layout. Flow layout is based on `inline` elements and `block` elements. Inline elements display one after the other, starting on the left, and block elements start at the top and move down the page. 

If you think about a newspaper this makes sense. Block elements are like paragraphs that are stacked on top of each other. Inline elements like `<strong>` do not stack. They just sit in the flow of the text from left to right. By default, most elements are `block`.

The significant exception is `<button>`. Buttons are inline elements but if you were to give it a margin-top, it would take effect, unlike a `span`. Weird!

Block elements like `h1` and `p` and `div` will expand to fill the available space.

## Flex Layout

The default flow layout is great for the original purpose of HTML & CSS - namely laying documents out a bit like a newspaper. 

However, as the web has developed, user interfaces have become increasingly complex. Probably the best and easiest approach to layout is the `flex layout` (A.K.A Flexbox).

For a good understanding of Flexbox, checkout the first half of [this interactive guide](https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/) (up to but not including "Hypothetical size")

Play [Flexbox Froggy](https://flexboxfroggy.com/) for practice!

## Common Layout Formulas

A collection of popular layouts and patterns made with CSS can be found [here](https://csslayout.io/).

### Further resources

- [MDN Concepts of Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox)
- [Optional CSS Exercises](https://github.com/TheOdinProject/css-exercises)
