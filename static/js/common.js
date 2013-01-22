jax = {
	call: function(method, params, elements) {
		uri = location.href;
		params = params || {};
		if(typeof(params) == 'string') {
			params += "&method=" + method;
		} else {
			params['method'] = method;
		}
		$.post(uri, params, function(response){
			if(elements !== undefined) {
				if (!$.isArray(elements)) {
					elements = new Array(elements);
				};
				var sections = response.split("\n\n\n~~~\n\n\n");
				var min_length = Math.min(elements.length, sections.length);
				for (var i = 0; i < min_length; i++) {
					$(elements[i]).html(sections[i]);
				};
			}
		});
	}
};

////////////////////////////////////////////////////////////////////////////////
//	FORM SERIALIZATION FUNCTION THAT ALWAYS INCLUDES CHECKBOXES, CHECKED OR NOT
(function($){
	$.fn.formValues = function(options) {
		var settings = {
			on: '1',
			off: ''
		};
		if (options) {
			settings = $.extend(settings, options);
		}
		var $container = $(this).eq(0),
			$checkboxes = $container.find("input[type='checkbox']").each(function() {
				$(this).attr('value', this.checked ? settings.on : settings.off).attr('checked', true);
			});
		var s = ($container.serialize());
		$checkboxes.each(function() {
			var $this = $(this);
			$this.attr('checked', $this.val() == settings.on ? true : false);
		});
		return s;
	};
})(jQuery);


////////////////////////////////////////////////////////////////////////////////
//	RESIZE ELEMENTS WITH CLASS '_fillbox' TO ALWAYS FILL THEIR PARENT'S REMAINING SPACE
function __resizeToFillContainer() {
	$('._fillbox').each(function(){

		var pHeight				= parseInt( $(this).parent().innerHeight(), 10 );
		var bTop				= parseInt( $(this).offset().top, 10 );
		var bMargin				= parseInt( $(this).css("marginTop"), 10 ) + parseInt( $(this).css("marginBottom"), 10 );
		var bPadding			= parseInt( $(this).css("paddingTop"), 10 ) + parseInt( $(this).css("paddingBottom"), 10 );
		var bBorder				= parseInt( $(this).css("borderTopWidth"), 10 ) + parseInt( $(this).css("borderBottomWidth"), 10 );
		var bExtras				= parseInt( bMargin + bPadding + bBorder, 10 );
		var newHeight			= parseInt( pHeight - bTop - bExtras, 10 );

		$(this).height( newHeight );
	});
}
$(window).load(__resizeToFillContainer);
$(window).resize(__resizeToFillContainer);
