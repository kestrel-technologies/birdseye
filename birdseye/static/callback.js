// Salesforce returns the token in the fragment; hand it to the server.
var p = new URLSearchParams(window.location.hash.substring(1));
window.location.replace("/oauth/callback?access_token=" + encodeURIComponent(p.get("access_token")) + "&instance_url=" + encodeURIComponent(p.get("instance_url")));
