const navigator = document.querySelector('#myNavigator');

document.addEventListener('init', function(event) {
  
  var page = event.target;
  console.log(page)

  if (page.id === 'page1') {
    // eventos de la página 1
    page.querySelector('#push-button').onclick = function() {
      navigator.pushPage('page2.html', {data: {title: 'Page 2'}});
    };

  } else if (page.id === 'page2') {
    // eventos de la página 2
    page.querySelector('ons-toolbar .center').innerHTML = page.data.title;

    const btn_ir_a_3 = page.querySelector('.ir-a-3')
    btn_ir_a_3.onclick = function() {
      // tengo que dirigirme a la página 3
      navigator.pushPage('page3.html')
    }
  }

});