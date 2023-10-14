# HTML Forms

HTML forms are a fundamental part of web development, allowing users to interact with and submit data to a website. 

Forms are used for a wide range of purposes, such as collecting user information, accepting user feedback, and enabling online transactions. Let's walk through the process of creating an HTML form step by step:

You can add the following code in your `index.html`

## Step 1: Setting up the Form Structure

Start by creating the basic structure of the form using the `<form>` element. Inside the `<form>` element, you'll include various form controls such as <strong>input fields, checkboxes, radio buttons, dropdown lists, and buttons</strong>. Here's an example:


```html
<form action="/tasks" method="POST">
  <!-- Form controls go here -->
</form>
```

In the example above, the action attribute specifies the URL or file where the form data will be submitted, and the method attribute defines the HTTP method to be used (the default is GET). 

<strong>NOTE:</strong> Currently we don't have a `server` that would respond to a form submission so until we do, the method is redundant.

## Step 2: Adding Form Controls

Inside the `<form>` element, you'll include different form controls based on your requirements. Here are some commonly used form controls:

### Text Input

Use the `<input>` element with the `type="text"` attribute for single-line text input.

```html
<label for="name">Name:</label>
<input type="text" id="name" name="name" placeholder="Enter your name">
```

The `<label>` element is used to associate a label with a form control. The `for` attribute specifies the id of the related form control. In this case, the label is associated with the text input field with the id of "name". The text "Name:" will be displayed as the label for the input field.

The `<input>` element is used to create various form controls, and in this case, it is used to create a text input field. The `type="text"` attribute specifies that it is a single-line text input field.

The `id` attribute uniquely identifies the input field. It is used to associate the `<label>` element with the input field.

The `name` attribute is used to provide a name for the form control. When the form is submitted, this name will be used to identify the input field and its corresponding value.

### Dropdown List

 Use the `<select>` element to create a dropdown list of options.

 ```html
<label for="pizza-flavour">Select an option:</label>
<select id="pizza-flavour" name="pizza-flavour">
  <option value="pepperoni">Pepperoni</option>
  <option value="veg-feast">Veg Feast</option>
</select>
 ```

Similar to the previous example, the `<label>` element is used to associate a label with a form control. The `for` attribute specifies the id of the related form control. In this case, the label is associated with the dropdown list with the id of `pizza-flavour`. The text "Select an option:" will be displayed as the label for the dropdown list.

The `<select>` element is used to create a dropdown list of options.

The id attribute uniquely identifies the dropdown list. It is used to associate the <label> element with the dropdown list.

 The name attribute provides a name for the dropdown list. When the form is submitted, this name will be used to identify the selected option and its corresponding value.

The `<option>` element is used to define an option within the dropdown list.

The value attribute specifies the value associated with the option. This value will be sent to the server when the form is submitted.

The text between the opening and closing `<option>` tags is the visible text that represents the option in the dropdown list.


### Radio Buttons 

Use the `<input>` element with type="radio" and the same name attribute for grouped options where the user can select only one.

```html
<label for="radio-1">BBC Radio 1</label>
<input type="radio" id="radio-1" name="station" value="radio-1">

<label for="radio-2">BBC Radio 2</label>
<input type="radio" id="radio-2" name="station" value="radio-2">

```

### Checkboxes

Use the `<input>` element with type="checkbox" for options where the user can select multiple choices.

```html
<label for="email">Email</label>
<input type="checkbox" id="email" name="email" value="1">

<label for="text-message">Text Message</label>
<input type="checkbox" id="text-message" name="text-message" value="2">

```

### Textarea

Use the `<textarea>` element for multi-line text input.

```html
<label for="message">Message:</label>
<textarea id="message" name="message" rows="4" cols="30"></textarea>
```

### Submit Button

The markup for our form is almost complete; we just need to add a button to allow the user to send, or "submit", their data once they have filled out the form. This is done by using the `<button>` element.

(You can also use the `<input>` element with type="submit" to create a button to submit the form)

```html
<button type="submit">Send your message</button>
```

### Accessibility

[How to write accessible forms](https://www.a11yproject.com/posts/how-to-write-accessible-forms/)

### Complete Form Example

Your completed form should now look like this:

```html
    <form action="/tasks" method="POST">
      <!-- Form controls go here -->
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" placeholder="Enter your name" />

      <!-- Dropdown list -->
      <label for="pizza-flavour">Select an option:</label>
      <select id="pizza-flavour" name="pizza-flavour">
        <option value="pepperoni">Pepperoni</option>
        <option value="veg-feast">Veg Feast</option>
      </select>

      <!-- Radio buttons -->
      <label for="radio-1">BBC Radio 1</label>
      <input type="radio" id="radio-1" name="station" value="radio-1" />

      <label for="radio-2">BBC Radio 2</label>
      <input type="radio" id="radio-2" name="station" value="radio-2" />

      <!-- Checkboxes -->
      <label for="email">Email</label>
      <input type="checkbox" id="email" name="email" value="1" />

      <label for="text-message">Text Message</label>
      <input type="checkbox" id="text-message" name="text-message" value="2" />

      <!-- Textarea -->
      <label for="message">Message:</label>
      <textarea id="message" name="message" rows="4" cols="30"></textarea>

      <!-- Submit button -->
      <button type="submit">Send your message</button>
    </form>
```

### Further resources

- [More on Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms/How_to_structure_a_web_form)

# Next Lesson
[Semantic HTML >>](./5_semantic_html.md)