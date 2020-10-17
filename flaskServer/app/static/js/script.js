$(document).ready(function() {

  function ajaxRequest(url, data) {
    $.ajax({
	  type: "POST",
	  url: url,
	  data: data,
	  dataType: 'application/json;charset=UTF-8'});
  }

  // main switch
  let $btnOn = $('#btn-on');
  let $btnOff = $('#btn-off');

  //on
  $btnOn.on('click', function() {
    let data = {'main_switch': 'on'};
    ajaxRequest('/', data);

	  $btnOn.removeClass("z-depth-5");
	  $btnOff.addClass("z-depth-5");
  });

  //off
  $btnOff.on('click', function() {
    let data = {'main_switch': 'off'};
    ajaxRequest('/', data);

	  $btnOff.removeClass("z-depth-5");
	  $btnOn.addClass("z-depth-5");
  });

  //save
  $('#btn-save').on('click', function() {
    let data = {'save': 'save'};
    ajaxRequest('/', data);
  });

	// brightness
	let $brightRange = $('#brightnessRange');
	let $brightSpan = $('#brightnessSpan');

  $brightSpan.html($brightRange.val());

  $brightRange.on('input change', () => {
    $brightSpan.html($brightRange.val());
  });

  $brightRange.on('change', function() {
    let data = {'brightness': $brightRange.val()};
    ajaxRequest('/', data);
  });

  // static-mode
  // static-red
  let $staticRedRange = $('#static-red-range');
  let $staticRedSpan = $('#static-red-span');

  $staticRedSpan.html($staticRedRange.val());

  $staticRedRange.on('input change', () => {
    $staticRedSpan.html($staticRedRange.val());
  });

  $staticRedRange.on('click', function() {
    let data = {'static_red': $staticRedRange.val()};
    ajaxRequest('/static-mode/', data);
  });

  // static-green
  let $staticGreenRange = $('#static-green-range');
  let $staticGreenSpan = $('#static-green-span');

  $staticGreenSpan.html($staticGreenRange.val());

  $staticGreenRange.on('input change', () => {
    $staticGreenSpan.html($staticGreenRange.val());
  });

  $staticGreenRange.on('change', function() {
    let data = {'static_green': $staticGreenRange.val()};
    ajaxRequest('/static-mode/', data);
  });

  // static-blue
  let $staticBlueRange = $('#static-blue-range');
  let $staticBlueSpan = $('#static-blue-span');

  $staticBlueSpan.html($staticBlueRange.val());

  $staticBlueRange.on('input change', () => {
    $staticBlueSpan.html($staticBlueRange.val());
  });

  $staticBlueRange.on('change', function() {
    let data = {'static_blue': $staticBlueRange.val()};
    ajaxRequest('/static-mode/', data);
  });

  // palette
  let $paletteStatic = $('#paletteStatic');
  $paletteStatic.css('background-color',
                     `rgb(${$staticRedRange.val()},${$staticGreenRange.val()}, ${$staticBlueRange.val()})`)
  $('#static-red-range, #static-green-range, #static-blue-range').on('input change', () => {
    $paletteStatic.css('background-color',
                       `rgb(${$staticRedRange.val()}, ${$staticGreenRange.val()}, ${$staticBlueRange.val()})`)
  });

  // rainbow-mode
  // rainbow-step
  let $rainbowStepRange = $('#rainbow-step-range');
  let $rainbowStepSpan = $('#rainbow-step-span');

  $rainbowStepSpan.html($rainbowStepRange.val());

  $rainbowStepRange.on('input change', () => {
    $rainbowStepSpan.html($rainbowStepRange.val());
  });

  $rainbowStepRange.on('change', function() {
    let data = {'rainbow_step': $rainbowStepRange.val()};
    ajaxRequest('/rainbow-mode/', data);
  });

  // breath-mode
  // min-brightness
  let $breathMinBrightRange = $('#breath-min-brightness-range');
  let $breathMinBrightSpan = $('#breath-min-brightness-span');
  let $breathMaxBrightRange = $('#breath-max-brightness-range');
  let $breathMaxBrightSpan = $('#breath-max-brightness-span');

  $breathMinBrightSpan.html($breathMinBrightRange.val());

  $breathMinBrightRange.on('input change', () => {
    $breathMinBrightSpan.html($breathMinBrightRange.val());
  });

  $breathMinBrightRange.on('change', function() {
    let data = {'min_bright': $breathMinBrightRange.val()};
    ajaxRequest('/breath-mode/', data);
  });

   // max-brightness
  $breathMaxBrightSpan.html($breathMaxBrightRange.val());

  $breathMaxBrightRange.on('input change', () => {
    $breathMaxBrightSpan.html($breathMaxBrightRange.val());
  });

  $breathMaxBrightRange.on('change', function() {
    let data = {'max_bright': $breathMaxBrightRange.val()};
    ajaxRequest('/breath-mode/', data);
  });

  // breath-step
  let $breathStepRange = $('#breath-step-range');
  let $breathStepSpan = $('#breath-step-span');

  $breathStepSpan.html($breathStepRange.val());

  $breathStepRange.on('input change', () => {
    $breathStepSpan.html($breathStepRange.val());
  });

  $breathStepRange.on('change', function() {
    let data = {'breath_step': $breathStepRange.val()};
    ajaxRequest('/breath-mode/', data);
  });

  // breath-red
  let $breathRedRange = $('#breath-red-range');
  let $breathRedSpan = $('#breath-red-span');

  $breathRedSpan.html($breathRedRange.val());

  $breathRedRange.on('input change', () => {
    $breathRedSpan.html($breathRedRange.val());
  });

  $breathRedRange.on('change', function() {
    let data = {'breath_red': $breathRedRange.val()};
    ajaxRequest('/breath-mode/', data);
  });

  // breath-green
  let $breathGreenRange = $('#breath-green-range');
  let $breathGreenSpan = $('#breath-green-span');

  $breathGreenSpan.html($breathGreenRange.val());

  $breathGreenRange.on('input change', () => {
    $breathGreenSpan.html($breathGreenRange.val());
  });

  $breathGreenRange.on('change', function() {
    let data = {'breath_green': $breathGreenRange.val()};
    ajaxRequest('/breath-mode/', data);
  });

  // breath-blue
  let $breathBlueRange = $('#breath-blue-range');
  let $breathBlueSpan = $('#breath-blue-span');
  $breathBlueSpan.html($breathBlueRange.val());

  $breathBlueRange.on('input change', () => {
    $breathBlueSpan.html($breathBlueRange.val());
  });

  $breathBlueRange.change(function() {
    let data = {'breath_blue': $breathBlueRange.val()};
    ajaxRequest('/breath-mode/', data);
  });

  // palette
  let $paletteBreath = $('#paletteBreath');
  $paletteBreath.css('background-color',
                     `rgb(${$breathRedRange.val()}, ${$breathGreenRange.val()}, ${$breathBlueRange.val()})`)

  $('#breath-red-range, #breath-green-range, #breath-blue-range').on('input change', () => {
    $paletteBreath.css('background-color',
                     `rgb(${$breathRedRange.val()}, ${$breathGreenRange.val()}, ${$breathBlueRange.val()})`)
  });
});
