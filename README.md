# OneLoginOneTap
{
    "strict": true,
    "debug": true,
    "sp": {
        "entityId": "https://<domain>:8000/metadata/",
        "assertionConsumerService": {
            "url": "https://<domain>:8000/?acs",
            "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
        },
        "singleLogoutService": {
            "url": "https://<domain>:8000/?sls",
            "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
        },
        "NameIDFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
        "x509cert": "",
        "privateKey": ""
    },
	"idp": {
		"entityId": "https://app.onelogin.com/saml/metadata/123456",
		"singleSignOnService": {
			"url": "https://domain.onelogin.com/trust/saml2/http-post/sso/123456",
			"binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
		},
		"singleLogoutService": {
			"url": "https://domain.onelogin.com/trust/saml2/http-redirect/slo/123456",
			"binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
		},
		"x509cert": "XXXXxXXX1xXxXXXxXXXXXXxXXxxXx..."
	}
}