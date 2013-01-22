/**
 * Copyright (c) 2003-2012, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

function d(o) {
	s = '';
	for(p in o) {
		s = p + ": " + o[p] + "\n";
	}
}
CKEDITOR.editorConfig = function( config ) {
	config.autoGrow_onStartup = true;
	config.browserContextMenuOnCtrl = true;
	config.fullPage = false;
	config.toolbarCanCollapse = false;
	config.removePlugins = 'elementspath';
	config.resize_enabled = false;
	config.uiColor = '#eee';
	config.width = '100%';
	config.height = '500'
	config.toolbar = [
		{ name: 'document',    items : [ 'Source','Templates','ShowBlocks','-','Maximize' ] },
		{ name: 'clipboard',   items : [ 'Undo','Redo','-','Cut','Copy','Paste','PasteText','SelectAll','RemoveFormat','-','Find','Replace' ] },
		{ name: 'paragraph',   items : [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote','CreateDiv','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock' ] },
		'/',
		{ name: 'basicstyles', items : [ 'Bold','Italic','Underline','Strike','Subscript','Superscript','TextColor','BGColor' ] },
		{ name: 'styles',      items : [ 'Font','FontSize','Format' ] },
		{ name: 'links',       items : [ 'Link','Unlink','Anchor','Image','Flash','Table','HorizontalRule' ] }
	];
};
