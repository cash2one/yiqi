(function($) {
	/**
	 * 表单扩展工具集
	 */
	$.formUtils = {
		formData : function(form) {
			var data = {};
			$(form).find('input,textarea,select').filter(':not([type="submit"],[type="reset"],[type="button"])').each(function() {
				if ($(this).attr('type') == 'radio') {
					if ($(this).attr("checked") == 'checked') {
						data[this.name] = $.trim($(this).val());
					}
				} else if ($(this).attr('type') == 'checkbox') {
					if ($(this).attr("checked") == 'checked') {
						if ( typeof data[this.name] == 'undefined') {
							data[this.name] = $.trim($(this).val());
						} else {
							data[this.name] = data[this.name].split('|');
							data[this.name].push($.trim($(this).val()));
							data[this.name] = data[this.name].join('|');
						}
					}
				} else {
					data[this.name] = $.trim($(this).val());
				}
			});
			return data;
		},
		/**
		 * Available validators
		 */
		validators : {},
		addValidator : function(validator) {
			this.validators[validator.name] = {
				name : validator.name,
				fn : validator.fn,
				msg : validator.msg || '不正确',
				params : validator.params || {},
				acceptEmpty : ( typeof validator.acceptEmpty == 'undefined') ? true : validator.acceptEmpty
			};
		},
		empty : function(obj) {
			return typeof obj == 'undefined' || obj === null || obj === '';
		}
	};

	$.fn.validationSetup = function(setting) {
		var $form = $(this);
		var success = function(field, msg) {
			$(field).next().remove();
			$(field).parent().parent().removeClass('error');
		};

		var error = function(field, msg) {
			$(field).next().remove();
			var cgrp = $(field).parent().parent();
			cgrp.removeClass('success').addClass('error');
			var label = cgrp.find('label').html() + ' ';
			var span = $('<span class="help-inline">').append(label + msg);
			$(field).parent().append(span);
		};

		var help = function(field, msg) {
			var cgrp = $(field).parent().parent();
			$(field).next().remove();
			cgrp.removeClass('success').removeClass('error');
			var span = $('<span class="help-inline">').append(msg);
			$(field).parent().append(span);
		};

		var config = $.extend({
			ruleAttribute : 'data-validation', // name of the attribute holding the validation rules
			errorMsgAttribute : 'data-validation-error-msg',
			helpMsgAttribute : 'data-validation-help',
			validateOnBlur : true,
			showHelpOnFocus : true,
			successFn : success,
			errorFn : error,
			helpFn : help
		}, setting || {});

		if (config.validateOnBlur) {
			$form.find('input[' + config.ruleAttribute + '], textarea[' + config.ruleAttribute + ']').blur(function() {
				$(this).validateInput(config);
			});
		}

		if (config.showHelpOnFocus) {
			$form.find('input[' + config.helpMsgAttribute + '], textarea[' + config.helpMsgAttribute + ']').focus(function() {
				config.helpFn(this, $(this).attr(config.helpMsgAttribute));
			});
		}

		$form.check = function() {
			var result = true;
			$form.find('input[' + config.ruleAttribute + '], textarea[' + config.ruleAttribute + ']').each(function() {
				if (!$(this).validateInput(config)) {
					result = false;
				}
			});
			return result;
		};

		return $form;
	};

	$.fn.validateInput = function(config) {
		var msg = ' ';
		var result = true;
		var errorMsg = $(this).attr(config.errorMsgAttribute);
		var validationRules = $(this).attr(config.ruleAttribute).split(" ");
		for (var i in validationRules) {
			var vdtor = $.formUtils.validators[validationRules[i]];
			if (vdtor && typeof vdtor['fn'] == 'function') {
				var res = (vdtor['acceptEmpty'] && $(this).val() === '') || vdtor.fn(this, $(this).val(), vdtor['params']);
				if (!res) {
					msg = msg + vdtor.msg + ' ';
					result = false;
				}
			} else {
				console.warn('Using undefined validator "' + validationRules[i] + '"');
			}
		}

		msg = $.formUtils.empty(errorMsg) ? msg : errorMsg;

		if (result) {
			config.successFn(this, msg);
		} else {
			config.errorFn(this, msg);
		}
		return result;
	};

	$.formUtils.addValidator({
		name : 'require',
		fn : function(field, value, params) {
			return !$.formUtils.empty(value) && !( typeof value.length !== 'undefined' && value.length === 0);
		},
		msg : '不能为空',
		acceptEmpty : false
	});

	$.formUtils.addValidator({
		name : 'numeric',
		fn : function(field, value, params) {
			return /^\d*$/.test(value);
		}
	});

	$.formUtils.addValidator({
		name : 'email',
		fn : function(field, value, params) {
			return /^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/.test(value);
		}
	});
	
	$.formUtils.addValidator({
		name : 'phone',
		fn : function(field, value, params) {
			return /^0{0,1}(13|15|18)[0-9]{9}$/.test(value);
		}
	});
	
	$.formUtils.addValidator({
		name : 'idcard',
		fn : function(field, value, params) {
			return /^\d{14}\w{4}$/.test(value);
		}
	});

})(jQuery);

