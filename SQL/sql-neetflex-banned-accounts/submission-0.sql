-- ban == login same for two IP addresses
-- any order

SELECT DISTINCT a.account_id
FROM log_info a
JOIN log_info b 
    ON a.account_id = b.account_id
    AND a.ip_address != b.ip_address        -- different IPs
    AND a.login BETWEEN b.login AND b.logout -- a's login falls inside b's session
ORDER BY account_id;