<?php 
/**
 * Plugin Name: Custom Yoast API
 * Description: A custom API to update Yoast SEO metadata via REST API.
 * Version: 1.0.1
 * Author: Harmon Digital, LLC
 */

add_action('rest_api_init', function () {
    register_rest_route('custom-yoast-api/v1', '/update-meta/', array(
        'methods' => 'POST',
        'callback' => 'custom_yoast_api_update_meta',
        'permission_callback' => function () {
            return current_user_can('edit_posts');
        }
    ));
});

function custom_yoast_api_update_meta($request) {
    $post_id = $request['post_id'];
    $seo_title = $request['seo_title'];
    $seo_description = $request['seo_description'];
    $focus_keyphrase = $request['focus_keyphrase']; // New line for focus keyphrase

    update_post_meta($post_id, '_yoast_wpseo_title', $seo_title);
    update_post_meta($post_id, '_yoast_wpseo_metadesc', $seo_description);
    update_post_meta($post_id, '_yoast_wpseo_focuskw', $focus_keyphrase); // Update focus keyphrase

    return new WP_REST_Response('Yoast SEO Data Updated', 200);
}
