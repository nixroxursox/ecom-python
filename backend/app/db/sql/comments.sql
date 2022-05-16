-- name: get-comments-for-article-by-slug
SELECT
    C.id,
    C.body,
    C.created_at,
    C.updated_at,
    (
        SELECT
            username
        FROM
            users
        WHERE
            id = C.author_id
    ) AS author_username
FROM
    commentaries C
    INNER JOIN articles A
    ON C.article_id = A.id
    AND (
        A.slug = :slug
    );
-- name: get-comment-by-id-and-slug^
SELECT
    C.id,
    C.body,
    C.created_at,
    C.updated_at,
    (
        SELECT
            username
        FROM
            users
        WHERE
            id = C.author_id
    ) AS author_username
FROM
    commentaries C
    INNER JOIN articles A
    ON C.article_id = A.id
    AND (
        A.slug = :article_slug
    )
WHERE
    C.id = :comment_id;
-- name: create-new-comment<!
    WITH users_subquery AS (
        (
            SELECT
                id,
                username
            FROM
                users
            WHERE
                username = :author_username
        )
    )
INSERT INTO
    commentaries (
        BODY,
        author_id,
        article_id
    )
VALUES
    (
        :body,
        (
            SELECT
                id
            FROM
                users_subquery
        ),
        (
            SELECT
                id
            FROM
                articles
            WHERE
                slug = :article_slug
        )
    ) RETURNING id,
    BODY,
    (
        SELECT
            username
        FROM
            users_subquery
    ) AS author_username,
    created_at,
    updated_at;
-- name: delete-comment-by-id!
DELETE FROM
    commentaries
WHERE
    id = :comment_id
    AND author_id = (
        SELECT
            id
        FROM
            users
        WHERE
            username = :author_username
    );
