odoo.define('apollo_custom_web.toggle_password', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.TogglePassword = publicWidget.Widget.extend({
        selector: '.toggle-password',
        events: {
            'click': '_onTogglePassword',
        },

        /**
         * Called when the widget is mounted.
         */
        start: function () {
            this._super.apply(this, arguments);
            this._initializeState();
        },

        /**
         * Initializes the eye icon to the closed state and password field to "password".
         */
        _initializeState: function () {
            const passwordField = document.getElementById("password");
            const eyeIcon = this.$el;

            passwordField.type = "password"; // Default to hidden password
            eyeIcon.removeClass("fa-eye").addClass("fa-eye-slash"); // Default to closed eye
        },

        /**
         * Toggles the password field's visibility and updates the eye icon.
         */
        _onTogglePassword: function (ev) {
            const passwordField = document.getElementById("password");
            const eyeIcon = ev.currentTarget;

            // Toggle the password field's visibility
            if (passwordField.type === "password") {
                passwordField.type = "text"; // Show password
                eyeIcon.classList.remove("fa-eye-slash");
                eyeIcon.classList.add("fa-eye");
            } else {
                passwordField.type = "password"; // Hide password
                eyeIcon.classList.remove("fa-eye");
                eyeIcon.classList.add("fa-eye-slash");
            }
        },
    });
});
