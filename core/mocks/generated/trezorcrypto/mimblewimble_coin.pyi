from typing import *
from enum import IntEnum, IntFlag
from trezorcrypto.bip32 import HDNode
from apps.mimblewimble_coin.coins import CoinInfo
from trezor.enums import MimbleWimbleCoinSwitchType, MimbleWimbleCoinAddressType


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
class AddressDerivationType(IntEnum):
    """
    Address derivation type
    """
    MWC_ADDRESS_DERIVATION = 0
    GRIN_ADDRESS_DERIVATION = 1


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
class PaymentProofMessageType(IntEnum):
    """
    Payment proof message type
    """
    ASCII_PAYMENT_PROOF_MESSAGE = 0
    BINARY_PAYMENT_PROOF_MESSAGE = 1


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
class PaymentProofAddressType(IntFlag):
    """
    Payment proof address type
    """
    MQS_PAYMENT_PROOF_ADDRESS = 1 << 0
    TOR_PAYMENT_PROOF_ADDRESS = 1 << 1
    SLATEPACK_PAYMENT_PROOF_ADDRESS = 1 << 2


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
class SlateEncryptionType(IntFlag):
    """
    Slate encryption type
    """
    MQS_SLATE_ENCRYPTION = 1 << 0
    TOR_SLATE_ENCRYPTION = 1 << 1
    SLATEPACK_SLATE_ENCRYPTION = 1 << 2


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
class EncryptingOrDecryptingState(IntEnum):
    """
    Encrypting or decryption state
    """
    INACTIVE_STATE = 0
    READY_STATE = 1
    ACTIVE_STATE = 2
    COMPLETE_STATE = 3


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
class KernelFeatures(IntEnum):
    """
    Kernel features
    """
    PLAIN_FEATURES = 0
    COINBASE_FEATURES = 1
    HEIGHT_LOCKED_FEATURES = 2
    NO_RECENT_DUPLICATE_FEATURES = 3


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getRootPublicKey(extendedPrivateKey: HDNode) -> bytearray:
    """
    Get root public key
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getMqsAddress(extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int) -> str:
    """
    Get MQS address
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getTorAddress(extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int) -> str:
    """
    Get Tor address
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getSlatepackAddress(extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int) -> str:
    """
    Get Slatepack address
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getSeedCookie(extendedPrivateKey: HDNode) -> bytes:
    """
    Get seed cookie
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getCommitment(extendedPrivateKey: HDNode, value: int, identifier: bytes, switchType: MimbleWimbleCoinSwitchType) -> bytes:
    """
    Get commitment
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getBulletproofComponents(extendedPrivateKey: HDNode, value: int, identifier: bytes, switchType: MimbleWimbleCoinSwitchType, updateProgress: Callable[[int], None] | None) -> tuple[bytes, bytes, bytes]:
    """
    Get Bulletproof components
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isValidMqsAddressDomain(mqsAddressDomain: str) -> bool:
    """
    Is valid MQS address domain
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isValidMqsAddress(mqsAddress: str, coinInfo: CoinInfo) -> bool:
    """
    Is valid MQS address
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def startMqsEncryption(encryptionAndDecryptionContext: memoryview, extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int, recipientAddress: str, recipientAddressDomain: str | None) -> tuple[bytes, bytes]:
    """
    Start MQS encryption
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isValidTorAddress(torAddress: str) -> bool:
    """
    Is valid Tor address
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def startTorEncryption(encryptionAndDecryptionContext: memoryview, extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int, recipientAddress: str) -> bytes:
    """
    Start Tor encryption
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def encryptData(encryptionAndDecryptionContext: memoryview, data: bytes) -> bytes:
    """
    Encrypt data
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def finishEncryption(encryptionAndDecryptionContext: memoryview, extendedPrivateKey: HDNode, coinInfo: CoinInfo) -> tuple[bytes, bytes | None]:
    """
    Finish encryption
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def startMqsDecryption(encryptionAndDecryptionContext: memoryview, extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int, senderAddress: str, nonce: bytes, salt: bytes) -> None:
    """
    Start MQS decryption
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def startTorDecryption(encryptionAndDecryptionContext: memoryview, extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int, senderAddress: str, nonce: bytes) -> None:
    """
    Start Tor decryption
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isValidX25519PublicKey(x25519PublicKey: bytes) -> bool:
    """
    Is valid X25519 public key
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def startSlatepackDecryption(encryptionAndDecryptionContext: memoryview, extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int, ephemeralX25519PublicKey: bytes, nonce: bytes, encryptedFileKey: bytes, payloadNonce: bytes) -> None:
    """
    Start Slatepack decryption
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def decryptData(encryptionAndDecryptionContext: memoryview, encryptedData: bytes) -> bytes:
    """
    Decrypt data
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def finishDecryption(encryptionAndDecryptionContext: memoryview, tag: bytes) -> bytes:
    """
    Finish decryption
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isValidSlatepackAddress(slatepackAddress: str, coinInfo: CoinInfo) -> bool:
    """
    Is valid Slatepack address
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isZero(data: bytes) -> bool:
    """
    Is zero
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def startTransaction(transactionContext: memoryview, index: int, output: int, input: int, fee: int, secretNonceIndex: int, address: str) -> None:
    """
    Start transaction
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def includeOutputInTransaction(transactionContext: memoryview, extendedPrivateKey: HDNode, value: int, identifier: bytes, switchType: MimbleWimbleCoinSwitchType) -> None:
    """
    Include output in transaction
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def includeInputInTransaction(transactionContext: memoryview, extendedPrivateKey: HDNode, value: int, identifier: bytes, switchType: MimbleWimbleCoinSwitchType) -> None:
    """
    Include input in transaction
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isValidSecp256k1PrivateKey(privateKey: bytes) -> bool:
    """
    Is valid secp256k1 private key
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def applyOffsetToTransaction(transactionContext: memoryview, offset: bytes) -> int | None:
    """
    Apply offset to transaction
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getTransactionPublicKey(transactionContext: memoryview) -> bytes:
    """
    Get transaction public key
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getTransactionPublicNonce(transactionContext: memoryview) -> bytes:
    """
    Get transaction public nonce
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getTransactionMessageSignature(transactionContext: memoryview, message: str) -> bytes:
    """
    Get transaction message signature
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isValidSecp256k1PublicKey(publicKey: bytes) -> bool:
    """
    Is valid secp256k1 public key
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def isValidCommitment(commitment: bytes) -> bool:
    """
    Is valid commitment
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def verifyTransactionPaymentProof(transactionContext: memoryview, extendedPrivateKey: HDNode, coinInfo: CoinInfo, addressType: MimbleWimbleCoinAddressType, kernelCommitment: bytes, paymentProof: bytes) -> bool:
    """
    Verify transaction payment proof
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def finishTransaction(transactionContext: memoryview, extendedPrivateKey: HDNode, coinInfo: CoinInfo, addressType: MimbleWimbleCoinAddressType, publicNonce: bytes, publicKey: bytes, kernelInformation: bytes, kernelCommitment: bytes | None) -> tuple[bytes, bytes | None]:
    """
    Finish transaction
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getTimestampComponents(timestamp: int) -> tuple[int, int, int, int, int, int]:
    """
    Get timestamp components
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getMqsChallengeSignature(extendedPrivateKey: HDNode, coinInfo: CoinInfo, index: int, challenge: str) -> bytes:
    """
    Get MQS challenge signature
    """


# extmod/modtrezorcrypto/modtrezorcrypto-mimblewimble_coin.h
def getLoginChallengeSignature(extendedPrivateKey: HDNode, identifier: str, challenge: str) -> tuple[bytes, bytes]:
    """
    Get login challenge signature
    """
