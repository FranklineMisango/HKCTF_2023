import secretsharing

# Generate a random secret
original_secret = b'MySecret123'

# Split the secret into 5 shares, requiring any 3 to reconstruct the secret
shares = secretsharing.SecretSharer.split_secret(original_secret, 5, 3)

print("Shares:", shares)

# Combine any 3 shares to reconstruct the secret
reconstructed_secret = secretsharing.SecretSharer.recover_secret(shares[:3])

print("Reconstructed Secret:", reconstructed_secret)
