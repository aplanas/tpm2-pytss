"""
SPDX-License-Identifier: BSD-3
"""

from ._libtpm2_pytss import ffi, lib

from tpm2_pytss.utils import CLASS_INT_ATTRS_from_string, TPM2B_unpack


class TPM_FRIENDLY_INT(int):
    _FIXUP_MAP = {}

    @classmethod
    def parse(cls, value):
        # If it's a string initializer value, see if it matches anything in the list
        if isinstance(value, str):
            try:
                value = CLASS_INT_ATTRS_from_string(cls, value)
            except KeyError:
                raise RuntimeError(
                    f'Could not convert friendly name to value, got: "{value}"'
                )

        if not isinstance(value, int):
            raise RuntimeError(f'Expected int object, got: "{type(value)}"')

        return value


class TPM_FRIENDLY_INTLIST(TPM_FRIENDLY_INT):
    @classmethod
    def parse(cls, value):

        intvalue = 0

        if value is None:
            raise RuntimeError(f'Expected int object, got: "{type(value)}"')

        if len(value) == 0:
            raise RuntimeError(
                f'Could not convert friendly name to value, got: "{value}"'
            )

        # If it's a string initializer value, see if it matches anything in the list
        if isinstance(value, str):
            hunks = value.split("|") if "|" in value else [value]
            for k in hunks:
                try:
                    intvalue |= CLASS_INT_ATTRS_from_string(cls, k, cls._FIXUP_MAP)
                except KeyError:
                    raise RuntimeError(
                        f'Could not convert friendly name to value, got: "{k}"'
                    )

        return super().parse(intvalue)


class ESYS_TR(TPM_FRIENDLY_INT):
    NONE = lib.ESYS_TR_NONE
    PASSWORD = lib.ESYS_TR_PASSWORD
    PCR0 = lib.ESYS_TR_PCR0
    PCR1 = lib.ESYS_TR_PCR1
    PCR2 = lib.ESYS_TR_PCR2
    PCR3 = lib.ESYS_TR_PCR3
    PCR4 = lib.ESYS_TR_PCR4
    PCR5 = lib.ESYS_TR_PCR5
    PCR6 = lib.ESYS_TR_PCR6
    PCR7 = lib.ESYS_TR_PCR7
    PCR8 = lib.ESYS_TR_PCR8
    PCR9 = lib.ESYS_TR_PCR9
    PCR10 = lib.ESYS_TR_PCR10
    PCR11 = lib.ESYS_TR_PCR11
    PCR12 = lib.ESYS_TR_PCR12
    PCR13 = lib.ESYS_TR_PCR13
    PCR14 = lib.ESYS_TR_PCR14
    PCR15 = lib.ESYS_TR_PCR15
    PCR16 = lib.ESYS_TR_PCR16
    PCR17 = lib.ESYS_TR_PCR17
    PCR18 = lib.ESYS_TR_PCR18
    PCR19 = lib.ESYS_TR_PCR19
    PCR20 = lib.ESYS_TR_PCR20
    PCR21 = lib.ESYS_TR_PCR21
    PCR22 = lib.ESYS_TR_PCR22
    PCR23 = lib.ESYS_TR_PCR23
    PCR24 = lib.ESYS_TR_PCR24
    PCR25 = lib.ESYS_TR_PCR25
    PCR26 = lib.ESYS_TR_PCR26
    PCR27 = lib.ESYS_TR_PCR27
    PCR28 = lib.ESYS_TR_PCR28
    PCR29 = lib.ESYS_TR_PCR29
    PCR30 = lib.ESYS_TR_PCR30
    PCR31 = lib.ESYS_TR_PCR31
    OWNER = lib.ESYS_TR_RH_OWNER
    NULL = lib.ESYS_TR_RH_NULL
    LOCKOUT = lib.ESYS_TR_RH_LOCKOUT
    ENDORSEMENT = lib.ESYS_TR_RH_ENDORSEMENT
    PLATFORM = lib.ESYS_TR_RH_PLATFORM
    PLATFORM_NV = lib.ESYS_TR_RH_PLATFORM_NV
    RH_OWNER = lib.ESYS_TR_RH_OWNER
    RH_NULL = lib.ESYS_TR_RH_NULL
    RH_LOCKOUT = lib.ESYS_TR_RH_LOCKOUT
    RH_ENDORSEMENT = lib.ESYS_TR_RH_ENDORSEMENT
    RH_PLATFORM = lib.ESYS_TR_RH_PLATFORM
    RH_PLATFORM_NV = lib.ESYS_TR_RH_PLATFORM_NV


class TPM2_ALG(TPM_FRIENDLY_INT):
    ERROR = lib.TPM2_ALG_ERROR
    RSA = lib.TPM2_ALG_RSA
    SHA = lib.TPM2_ALG_SHA
    SHA1 = lib.TPM2_ALG_SHA1
    HMAC = lib.TPM2_ALG_HMAC
    AES = lib.TPM2_ALG_AES
    MGF1 = lib.TPM2_ALG_MGF1
    KEYEDHASH = lib.TPM2_ALG_KEYEDHASH
    XOR = lib.TPM2_ALG_XOR
    SHA256 = lib.TPM2_ALG_SHA256
    SHA384 = lib.TPM2_ALG_SHA384
    SHA512 = lib.TPM2_ALG_SHA512
    NULL = lib.TPM2_ALG_NULL
    SM3_256 = lib.TPM2_ALG_SM3_256
    SM4 = lib.TPM2_ALG_SM4
    RSASSA = lib.TPM2_ALG_RSASSA
    RSAES = lib.TPM2_ALG_RSAES
    RSAPSS = lib.TPM2_ALG_RSAPSS
    OAEP = lib.TPM2_ALG_OAEP
    ECDSA = lib.TPM2_ALG_ECDSA
    ECDH = lib.TPM2_ALG_ECDH
    ECDAA = lib.TPM2_ALG_ECDAA
    SM2 = lib.TPM2_ALG_SM2
    ECSCHNORR = lib.TPM2_ALG_ECSCHNORR
    ECMQV = lib.TPM2_ALG_ECMQV
    KDF1_SP800_56A = lib.TPM2_ALG_KDF1_SP800_56A
    KDF2 = lib.TPM2_ALG_KDF2
    KDF1_SP800_108 = lib.TPM2_ALG_KDF1_SP800_108
    ECC = lib.TPM2_ALG_ECC
    SYMCIPHER = lib.TPM2_ALG_SYMCIPHER
    CAMELLIA = lib.TPM2_ALG_CAMELLIA
    CTR = lib.TPM2_ALG_CTR
    SHA3_256 = lib.TPM2_ALG_SHA3_256
    SHA3_384 = lib.TPM2_ALG_SHA3_384
    SHA3_512 = lib.TPM2_ALG_SHA3_512
    OFB = lib.TPM2_ALG_OFB
    CBC = lib.TPM2_ALG_CBC
    CFB = lib.TPM2_ALG_CFB
    ECB = lib.TPM2_ALG_ECB
    FIRST = lib.TPM2_ALG_FIRST
    LAST = lib.TPM2_ALG_LAST


TPM2_ALG_ID = TPM2_ALG


class TPM2_ECC(TPM_FRIENDLY_INT):
    NONE = lib.TPM2_ECC_NONE
    NIST_P192 = lib.TPM2_ECC_NIST_P192
    NIST_P224 = lib.TPM2_ECC_NIST_P224
    NIST_P256 = lib.TPM2_ECC_NIST_P256
    NIST_P384 = lib.TPM2_ECC_NIST_P384
    NIST_P521 = lib.TPM2_ECC_NIST_P521
    BN_P256 = lib.TPM2_ECC_BN_P256
    BN_P638 = lib.TPM2_ECC_BN_P638
    SM2_P256 = lib.TPM2_ECC_SM2_P256


TPM2_ECC_CURVE = TPM2_ECC


class TPM2_CC(TPM_FRIENDLY_INT):
    NV_UndefineSpaceSpecial = lib.TPM2_CC_NV_UndefineSpaceSpecial
    FIRST = lib.TPM2_CC_FIRST
    EvictControl = lib.TPM2_CC_EvictControl
    HierarchyControl = lib.TPM2_CC_HierarchyControl
    NV_UndefineSpace = lib.TPM2_CC_NV_UndefineSpace
    ChangeEPS = lib.TPM2_CC_ChangeEPS
    ChangePPS = lib.TPM2_CC_ChangePPS
    Clear = lib.TPM2_CC_Clear
    ClearControl = lib.TPM2_CC_ClearControl
    ClockSet = lib.TPM2_CC_ClockSet
    HierarchyChangeAuth = lib.TPM2_CC_HierarchyChangeAuth
    NV_DefineSpace = lib.TPM2_CC_NV_DefineSpace
    PCR_Allocate = lib.TPM2_CC_PCR_Allocate
    PCR_SetAuthPolicy = lib.TPM2_CC_PCR_SetAuthPolicy
    PP_Commands = lib.TPM2_CC_PP_Commands
    SetPrimaryPolicy = lib.TPM2_CC_SetPrimaryPolicy
    FieldUpgradeStart = lib.TPM2_CC_FieldUpgradeStart
    ClockRateAdjust = lib.TPM2_CC_ClockRateAdjust
    CreatePrimary = lib.TPM2_CC_CreatePrimary
    NV_GlobalWriteLock = lib.TPM2_CC_NV_GlobalWriteLock
    GetCommandAuditDigest = lib.TPM2_CC_GetCommandAuditDigest
    NV_Increment = lib.TPM2_CC_NV_Increment
    NV_SetBits = lib.TPM2_CC_NV_SetBits
    NV_Extend = lib.TPM2_CC_NV_Extend
    NV_Write = lib.TPM2_CC_NV_Write
    NV_WriteLock = lib.TPM2_CC_NV_WriteLock
    DictionaryAttackLockReset = lib.TPM2_CC_DictionaryAttackLockReset
    DictionaryAttackParameters = lib.TPM2_CC_DictionaryAttackParameters
    NV_ChangeAuth = lib.TPM2_CC_NV_ChangeAuth
    PCR_Event = lib.TPM2_CC_PCR_Event
    PCR_Reset = lib.TPM2_CC_PCR_Reset
    SequenceComplete = lib.TPM2_CC_SequenceComplete
    SetAlgorithmSet = lib.TPM2_CC_SetAlgorithmSet
    SetCommandCodeAuditStatus = lib.TPM2_CC_SetCommandCodeAuditStatus
    FieldUpgradeData = lib.TPM2_CC_FieldUpgradeData
    IncrementalSelfTest = lib.TPM2_CC_IncrementalSelfTest
    SelfTest = lib.TPM2_CC_SelfTest
    Startup = lib.TPM2_CC_Startup
    Shutdown = lib.TPM2_CC_Shutdown
    StirRandom = lib.TPM2_CC_StirRandom
    ActivateCredential = lib.TPM2_CC_ActivateCredential
    Certify = lib.TPM2_CC_Certify
    PolicyNV = lib.TPM2_CC_PolicyNV
    CertifyCreation = lib.TPM2_CC_CertifyCreation
    Duplicate = lib.TPM2_CC_Duplicate
    GetTime = lib.TPM2_CC_GetTime
    GetSessionAuditDigest = lib.TPM2_CC_GetSessionAuditDigest
    NV_Read = lib.TPM2_CC_NV_Read
    NV_ReadLock = lib.TPM2_CC_NV_ReadLock
    ObjectChangeAuth = lib.TPM2_CC_ObjectChangeAuth
    PolicySecret = lib.TPM2_CC_PolicySecret
    Rewrap = lib.TPM2_CC_Rewrap
    Create = lib.TPM2_CC_Create
    ECDH_ZGen = lib.TPM2_CC_ECDH_ZGen
    HMAC = lib.TPM2_CC_HMAC
    Import = lib.TPM2_CC_Import
    Load = lib.TPM2_CC_Load
    Quote = lib.TPM2_CC_Quote
    RSA_Decrypt = lib.TPM2_CC_RSA_Decrypt
    HMAC_Start = lib.TPM2_CC_HMAC_Start
    SequenceUpdate = lib.TPM2_CC_SequenceUpdate
    Sign = lib.TPM2_CC_Sign
    Unseal = lib.TPM2_CC_Unseal
    PolicySigned = lib.TPM2_CC_PolicySigned
    ContextLoad = lib.TPM2_CC_ContextLoad
    ContextSave = lib.TPM2_CC_ContextSave
    ECDH_KeyGen = lib.TPM2_CC_ECDH_KeyGen
    EncryptDecrypt = lib.TPM2_CC_EncryptDecrypt
    FlushContext = lib.TPM2_CC_FlushContext
    LoadExternal = lib.TPM2_CC_LoadExternal
    MakeCredential = lib.TPM2_CC_MakeCredential
    NV_ReadPublic = lib.TPM2_CC_NV_ReadPublic
    PolicyAuthorize = lib.TPM2_CC_PolicyAuthorize
    PolicyAuthValue = lib.TPM2_CC_PolicyAuthValue
    PolicyCommandCode = lib.TPM2_CC_PolicyCommandCode
    PolicyCounterTimer = lib.TPM2_CC_PolicyCounterTimer
    PolicyCpHash = lib.TPM2_CC_PolicyCpHash
    PolicyLocality = lib.TPM2_CC_PolicyLocality
    PolicyNameHash = lib.TPM2_CC_PolicyNameHash
    PolicyOR = lib.TPM2_CC_PolicyOR
    PolicyTicket = lib.TPM2_CC_PolicyTicket
    ReadPublic = lib.TPM2_CC_ReadPublic
    RSA_Encrypt = lib.TPM2_CC_RSA_Encrypt
    StartAuthSession = lib.TPM2_CC_StartAuthSession
    VerifySignature = lib.TPM2_CC_VerifySignature
    ECC_Parameters = lib.TPM2_CC_ECC_Parameters
    FirmwareRead = lib.TPM2_CC_FirmwareRead
    GetCapability = lib.TPM2_CC_GetCapability
    GetRandom = lib.TPM2_CC_GetRandom
    GetTestResult = lib.TPM2_CC_GetTestResult
    Hash = lib.TPM2_CC_Hash
    PCR_Read = lib.TPM2_CC_PCR_Read
    PolicyPCR = lib.TPM2_CC_PolicyPCR
    PolicyRestart = lib.TPM2_CC_PolicyRestart
    ReadClock = lib.TPM2_CC_ReadClock
    PCR_Extend = lib.TPM2_CC_PCR_Extend
    PCR_SetAuthValue = lib.TPM2_CC_PCR_SetAuthValue
    NV_Certify = lib.TPM2_CC_NV_Certify
    EventSequenceComplete = lib.TPM2_CC_EventSequenceComplete
    HashSequenceStart = lib.TPM2_CC_HashSequenceStart
    PolicyPhysicalPresence = lib.TPM2_CC_PolicyPhysicalPresence
    PolicyDuplicationSelect = lib.TPM2_CC_PolicyDuplicationSelect
    PolicyGetDigest = lib.TPM2_CC_PolicyGetDigest
    TestParms = lib.TPM2_CC_TestParms
    Commit = lib.TPM2_CC_Commit
    PolicyPassword = lib.TPM2_CC_PolicyPassword
    ZGen_2Phase = lib.TPM2_CC_ZGen_2Phase
    EC_Ephemeral = lib.TPM2_CC_EC_Ephemeral
    PolicyNvWritten = lib.TPM2_CC_PolicyNvWritten
    PolicyTemplate = lib.TPM2_CC_PolicyTemplate
    CreateLoaded = lib.TPM2_CC_CreateLoaded
    PolicyAuthorizeNV = lib.TPM2_CC_PolicyAuthorizeNV
    EncryptDecrypt2 = lib.TPM2_CC_EncryptDecrypt2
    AC_GetCapability = lib.TPM2_CC_AC_GetCapability
    AC_Send = lib.TPM2_CC_AC_Send
    Policy_AC_SendSelect = lib.TPM2_CC_Policy_AC_SendSelect
    LAST = lib.TPM2_CC_LAST
    Vendor_TCG_Test = lib.TPM2_CC_Vendor_TCG_Test


class TPM2_SPEC(TPM_FRIENDLY_INT):
    FAMILY = lib.TPM2_SPEC_FAMILY
    LEVEL = lib.TPM2_SPEC_LEVEL
    VERSION = lib.TPM2_SPEC_VERSION
    YEAR = lib.TPM2_SPEC_YEAR
    DAY_OF_YEAR = lib.TPM2_SPEC_DAY_OF_YEAR


class TPM2_GENERATED_VALUE(TPM_FRIENDLY_INT):
    VALUE = lib.TPM2_GENERATED_VALUE


class TPM2_RC(TPM_FRIENDLY_INT):
    SUCCESS = lib.TPM2_RC_SUCCESS
    BAD_TAG = lib.TPM2_RC_BAD_TAG
    VER1 = lib.TPM2_RC_VER1
    INITIALIZE = lib.TPM2_RC_INITIALIZE
    FAILURE = lib.TPM2_RC_FAILURE
    SEQUENCE = lib.TPM2_RC_SEQUENCE
    PRIVATE = lib.TPM2_RC_PRIVATE
    HMAC = lib.TPM2_RC_HMAC
    DISABLED = lib.TPM2_RC_DISABLED
    EXCLUSIVE = lib.TPM2_RC_EXCLUSIVE
    AUTH_TYPE = lib.TPM2_RC_AUTH_TYPE
    AUTH_MISSING = lib.TPM2_RC_AUTH_MISSING
    POLICY = lib.TPM2_RC_POLICY
    PCR = lib.TPM2_RC_PCR
    PCR_CHANGED = lib.TPM2_RC_PCR_CHANGED
    UPGRADE = lib.TPM2_RC_UPGRADE
    TOO_MANY_CONTEXTS = lib.TPM2_RC_TOO_MANY_CONTEXTS
    AUTH_UNAVAILABLE = lib.TPM2_RC_AUTH_UNAVAILABLE
    REBOOT = lib.TPM2_RC_REBOOT
    UNBALANCED = lib.TPM2_RC_UNBALANCED
    COMMAND_SIZE = lib.TPM2_RC_COMMAND_SIZE
    COMMAND_CODE = lib.TPM2_RC_COMMAND_CODE
    AUTHSIZE = lib.TPM2_RC_AUTHSIZE
    AUTH_CONTEXT = lib.TPM2_RC_AUTH_CONTEXT
    NV_RANGE = lib.TPM2_RC_NV_RANGE
    NV_SIZE = lib.TPM2_RC_NV_SIZE
    NV_LOCKED = lib.TPM2_RC_NV_LOCKED
    NV_AUTHORIZATION = lib.TPM2_RC_NV_AUTHORIZATION
    NV_UNINITIALIZED = lib.TPM2_RC_NV_UNINITIALIZED
    NV_SPACE = lib.TPM2_RC_NV_SPACE
    NV_DEFINED = lib.TPM2_RC_NV_DEFINED
    BAD_CONTEXT = lib.TPM2_RC_BAD_CONTEXT
    CPHASH = lib.TPM2_RC_CPHASH
    PARENT = lib.TPM2_RC_PARENT
    NEEDS_TEST = lib.TPM2_RC_NEEDS_TEST
    NO_RESULT = lib.TPM2_RC_NO_RESULT
    SENSITIVE = lib.TPM2_RC_SENSITIVE
    MAX_FM0 = lib.TPM2_RC_MAX_FM0
    FMT1 = lib.TPM2_RC_FMT1
    ASYMMETRIC = lib.TPM2_RC_ASYMMETRIC
    ATTRIBUTES = lib.TPM2_RC_ATTRIBUTES
    HASH = lib.TPM2_RC_HASH
    VALUE = lib.TPM2_RC_VALUE
    HIERARCHY = lib.TPM2_RC_HIERARCHY
    KEY_SIZE = lib.TPM2_RC_KEY_SIZE
    MGF = lib.TPM2_RC_MGF
    MODE = lib.TPM2_RC_MODE
    TYPE = lib.TPM2_RC_TYPE
    HANDLE = lib.TPM2_RC_HANDLE
    KDF = lib.TPM2_RC_KDF
    RANGE = lib.TPM2_RC_RANGE
    AUTH_FAIL = lib.TPM2_RC_AUTH_FAIL
    NONCE = lib.TPM2_RC_NONCE
    PP = lib.TPM2_RC_PP
    SCHEME = lib.TPM2_RC_SCHEME
    SIZE = lib.TPM2_RC_SIZE
    SYMMETRIC = lib.TPM2_RC_SYMMETRIC
    TAG = lib.TPM2_RC_TAG
    SELECTOR = lib.TPM2_RC_SELECTOR
    INSUFFICIENT = lib.TPM2_RC_INSUFFICIENT
    SIGNATURE = lib.TPM2_RC_SIGNATURE
    KEY = lib.TPM2_RC_KEY
    POLICY_FAIL = lib.TPM2_RC_POLICY_FAIL
    INTEGRITY = lib.TPM2_RC_INTEGRITY
    TICKET = lib.TPM2_RC_TICKET
    BAD_AUTH = lib.TPM2_RC_BAD_AUTH
    EXPIRED = lib.TPM2_RC_EXPIRED
    POLICY_CC = lib.TPM2_RC_POLICY_CC
    BINDING = lib.TPM2_RC_BINDING
    CURVE = lib.TPM2_RC_CURVE
    ECC_POINT = lib.TPM2_RC_ECC_POINT
    WARN = lib.TPM2_RC_WARN
    CONTEXT_GAP = lib.TPM2_RC_CONTEXT_GAP
    OBJECT_MEMORY = lib.TPM2_RC_OBJECT_MEMORY
    SESSION_MEMORY = lib.TPM2_RC_SESSION_MEMORY
    MEMORY = lib.TPM2_RC_MEMORY
    SESSION_HANDLES = lib.TPM2_RC_SESSION_HANDLES
    OBJECT_HANDLES = lib.TPM2_RC_OBJECT_HANDLES
    LOCALITY = lib.TPM2_RC_LOCALITY
    YIELDED = lib.TPM2_RC_YIELDED
    CANCELED = lib.TPM2_RC_CANCELED
    TESTING = lib.TPM2_RC_TESTING
    REFERENCE_H0 = lib.TPM2_RC_REFERENCE_H0
    REFERENCE_H1 = lib.TPM2_RC_REFERENCE_H1
    REFERENCE_H2 = lib.TPM2_RC_REFERENCE_H2
    REFERENCE_H3 = lib.TPM2_RC_REFERENCE_H3
    REFERENCE_H4 = lib.TPM2_RC_REFERENCE_H4
    REFERENCE_H5 = lib.TPM2_RC_REFERENCE_H5
    REFERENCE_H6 = lib.TPM2_RC_REFERENCE_H6
    REFERENCE_S0 = lib.TPM2_RC_REFERENCE_S0
    REFERENCE_S1 = lib.TPM2_RC_REFERENCE_S1
    REFERENCE_S2 = lib.TPM2_RC_REFERENCE_S2
    REFERENCE_S3 = lib.TPM2_RC_REFERENCE_S3
    REFERENCE_S4 = lib.TPM2_RC_REFERENCE_S4
    REFERENCE_S5 = lib.TPM2_RC_REFERENCE_S5
    REFERENCE_S6 = lib.TPM2_RC_REFERENCE_S6
    NV_RATE = lib.TPM2_RC_NV_RATE
    LOCKOUT = lib.TPM2_RC_LOCKOUT
    RETRY = lib.TPM2_RC_RETRY
    NV_UNAVAILABLE = lib.TPM2_RC_NV_UNAVAILABLE
    NOT_USED = lib.TPM2_RC_NOT_USED
    H = lib.TPM2_RC_H
    P = lib.TPM2_RC_P
    S = lib.TPM2_RC_S
    RC1 = lib.TPM2_RC_1
    RC2 = lib.TPM2_RC_2
    RC3 = lib.TPM2_RC_3
    RC4 = lib.TPM2_RC_4
    RC5 = lib.TPM2_RC_5
    RC6 = lib.TPM2_RC_6
    RC7 = lib.TPM2_RC_7
    RC8 = lib.TPM2_RC_8
    RC9 = lib.TPM2_RC_9
    A = lib.TPM2_RC_A
    B = lib.TPM2_RC_B
    C = lib.TPM2_RC_C
    D = lib.TPM2_RC_D
    E = lib.TPM2_RC_E
    F = lib.TPM2_RC_F
    N_MASK = lib.TPM2_RC_N_MASK


class TPM2_EO(TPM_FRIENDLY_INT):
    EQ = lib.TPM2_EO_EQ
    NEQ = lib.TPM2_EO_NEQ
    SIGNED_GT = lib.TPM2_EO_SIGNED_GT
    UNSIGNED_GT = lib.TPM2_EO_UNSIGNED_GT
    SIGNED_LT = lib.TPM2_EO_SIGNED_LT
    UNSIGNED_LT = lib.TPM2_EO_UNSIGNED_LT
    SIGNED_GE = lib.TPM2_EO_SIGNED_GE
    UNSIGNED_GE = lib.TPM2_EO_UNSIGNED_GE
    SIGNED_LE = lib.TPM2_EO_SIGNED_LE
    UNSIGNED_LE = lib.TPM2_EO_UNSIGNED_LE
    BITSET = lib.TPM2_EO_BITSET
    BITCLEAR = lib.TPM2_EO_BITCLEAR


class TPM2_ST(TPM_FRIENDLY_INT):
    RSP_COMMAND = lib.TPM2_ST_RSP_COMMAND
    NULL = lib.TPM2_ST_NULL
    NO_SESSIONS = lib.TPM2_ST_NO_SESSIONS
    SESSIONS = lib.TPM2_ST_SESSIONS
    ATTEST_NV = lib.TPM2_ST_ATTEST_NV
    ATTEST_COMMAND_AUDIT = lib.TPM2_ST_ATTEST_COMMAND_AUDIT
    ATTEST_SESSION_AUDIT = lib.TPM2_ST_ATTEST_SESSION_AUDIT
    ATTEST_CERTIFY = lib.TPM2_ST_ATTEST_CERTIFY
    ATTEST_QUOTE = lib.TPM2_ST_ATTEST_QUOTE
    ATTEST_TIME = lib.TPM2_ST_ATTEST_TIME
    ATTEST_CREATION = lib.TPM2_ST_ATTEST_CREATION
    CREATION = lib.TPM2_ST_CREATION
    VERIFIED = lib.TPM2_ST_VERIFIED
    AUTH_SECRET = lib.TPM2_ST_AUTH_SECRET
    HASHCHECK = lib.TPM2_ST_HASHCHECK
    AUTH_SIGNED = lib.TPM2_ST_AUTH_SIGNED
    FU_MANIFEST = lib.TPM2_ST_FU_MANIFEST


class TPM2_SU(TPM_FRIENDLY_INT):
    CLEAR = lib.TPM2_SU_CLEAR
    STATE = lib.TPM2_SU_STATE


class TPM2_SE(TPM_FRIENDLY_INT):
    HMAC = lib.TPM2_SE_HMAC
    POLICY = lib.TPM2_SE_POLICY
    TRIAL = lib.TPM2_SE_TRIAL


class TPM2_CAP(TPM_FRIENDLY_INT):
    FIRST = lib.TPM2_CAP_FIRST
    ALGS = lib.TPM2_CAP_ALGS
    HANDLES = lib.TPM2_CAP_HANDLES
    COMMANDS = lib.TPM2_CAP_COMMANDS
    PP_COMMANDS = lib.TPM2_CAP_PP_COMMANDS
    AUDIT_COMMANDS = lib.TPM2_CAP_AUDIT_COMMANDS
    PCRS = lib.TPM2_CAP_PCRS
    TPM_PROPERTIES = lib.TPM2_CAP_TPM_PROPERTIES
    PCR_PROPERTIES = lib.TPM2_CAP_PCR_PROPERTIES
    ECC_CURVES = lib.TPM2_CAP_ECC_CURVES
    LAST = lib.TPM2_CAP_LAST
    VENDOR_PROPERTY = lib.TPM2_CAP_VENDOR_PROPERTY


class TPM2_PT(TPM_FRIENDLY_INT):
    NONE = lib.TPM2_PT_NONE
    GROUP = lib.TPM2_PT_GROUP
    FIXED = lib.TPM2_PT_FIXED


# TODO    FAMILY_INDICATOR = lib.TPM2_PT_FAMILY_INDICATOR
#    LEVEL = lib.TPM2_PT_LEVEL
#    REVISION = lib.TPM2_PT_REVISION
#    DAY_OF_YEAR = lib.TPM2_PT_DAY_OF_YEAR
#    YEAR = lib.TPM2_PT_YEAR
#    MANUFACTURER = lib.TPM2_PT_MANUFACTURER
#    VENDOR_STRING_1 = lib.TPM2_PT_VENDOR_STRING_1
#    VENDOR_STRING_2 = lib.TPM2_PT_VENDOR_STRING_2
#    VENDOR_STRING_3 = lib.TPM2_PT_VENDOR_STRING_3
#    VENDOR_STRING_4 = lib.TPM2_PT_VENDOR_STRING_4
#    VENDOR_TPM_TYPE = lib.TPM2_PT_VENDOR_TPM_TYPE
#    FIRMWARE_VERSION_1 = lib.TPM2_PT_FIRMWARE_VERSION_1
#    FIRMWARE_VERSION_2 = lib.TPM2_PT_FIRMWARE_VERSION_2
#    INPUT_BUFFER = lib.TPM2_PT_INPUT_BUFFER
#    TPM2_HR_TRANSIENT_MIN = lib.TPM2_PT_TPM2_HR_TRANSIENT_MIN
#    TPM2_HR_PERSISTENT_MIN = lib.TPM2_PT_TPM2_HR_PERSISTENT_MIN
#    HR_LOADED_MIN = lib.TPM2_PT_HR_LOADED_MIN
#    ACTIVE_SESSIONS_MAX = lib.TPM2_PT_ACTIVE_SESSIONS_MAX
#    PCR_COUNT = lib.TPM2_PT_PCR_COUNT
#    PCR_SELECT_MIN = lib.TPM2_PT_PCR_SELECT_MIN
#    CONTEXT_GAP_MAX = lib.TPM2_PT_CONTEXT_GAP_MAX
#    NV_COUNTERS_MAX = lib.TPM2_PT_NV_COUNTERS_MAX
#    NV_INDEX_MAX = lib.TPM2_PT_NV_INDEX_MAX
#    MEMORY = lib.TPM2_PT_MEMORY
#    CLOCK_UPDATE = lib.TPM2_PT_CLOCK_UPDATE
#    CONTEXT_HASH = lib.TPM2_PT_CONTEXT_HASH
#    CONTEXT_SYM = lib.TPM2_PT_CONTEXT_SYM
#    CONTEXT_SYM_SIZE = lib.TPM2_PT_CONTEXT_SYM_SIZE
#    ORDERLY_COUNT = lib.TPM2_PT_ORDERLY_COUNT
#    MAX_COMMAND_SIZE = lib.TPM2_PT_MAX_COMMAND_SIZE
#    MAX_RESPONSE_SIZE = lib.TPM2_PT_MAX_RESPONSE_SIZE
#    MAX_DIGEST = lib.TPM2_PT_MAX_DIGEST
#    MAX_OBJECT_CONTEXT = lib.TPM2_PT_MAX_OBJECT_CONTEXT
#    MAX_SESSION_CONTEXT = lib.TPM2_PT_MAX_SESSION_CONTEXT
#    PS_FAMILY_INDICATOR = lib.TPM2_PT_PS_FAMILY_INDICATOR
#    PS_LEVEL = lib.TPM2_PT_PS_LEVEL
#    PS_REVISION = lib.TPM2_PT_PS_REVISION
#    PS_DAY_OF_YEAR = lib.TPM2_PT_PS_DAY_OF_YEAR
#    PS_YEAR = lib.TPM2_PT_PS_YEAR
#    SPLIT_MAX = lib.TPM2_PT_SPLIT_MAX
#    TOTAL_COMMANDS = lib.TPM2_PT_TOTAL_COMMANDS
#    LIBRARY_COMMANDS = lib.TPM2_PTlibRARY_COMMANDS
#    VENDOR_COMMANDS = lib.TPM2_PT_VENDOR_COMMANDS
#    NV_BUFFER_MAX = lib.TPM2_PT_NV_BUFFER_MAX
#    MODES = lib.TPM2_PT_MODES
#    VAR = lib.TPM2_PT_VAR
#    PERMANENT = lib.TPM2_PT_PERMANENT
#    STARTUP_CLEAR = lib.TPM2_PT_STARTUP_CLEAR
#    TPM2_HR_NV_INDEX = lib.TPM2_PT_TPM2_HR_NV_INDEX
#    HR_LOADED = lib.TPM2_PT_HR_LOADED
#    HR_LOADED_AVAIL = lib.TPM2_PT_HR_LOADED_AVAIL
#    HR_ACTIVE = lib.TPM2_PT_HR_ACTIVE
#    HR_ACTIVE_AVAIL = lib.TPM2_PT_HR_ACTIVE_AVAIL
#    TPM2_HR_TRANSIENT_AVAIL = lib.TPM2_PT_TPM2_HR_TRANSIENT_AVAIL
#    TPM2_HR_PERSISTENT = lib.TPM2_PT_TPM2_HR_PERSISTENT
#    TPM2_HR_PERSISTENT_AVAIL = lib.TPM2_PT_TPM2_HR_PERSISTENT_AVAIL
#    NV_COUNTERS = lib.TPM2_PT_NV_COUNTERS
#    NV_COUNTERS_AVAIL = lib.TPM2_PT_NV_COUNTERS_AVAIL
#    ALGORITHM_SET = lib.TPM2_PT_ALGORITHM_SET
#    LOADED_CURVES = lib.TPM2_PT_LOADED_CURVES
#    LOCKOUT_COUNTER = lib.TPM2_PT_LOCKOUT_COUNTER
#    MAX_AUTH_FAIL = lib.TPM2_PT_MAX_AUTH_FAIL
#    LOCKOUT_INTERVAL = lib.TPM2_PT_LOCKOUT_INTERVAL
#    LOCKOUT_RECOVERY = lib.TPM2_PT_LOCKOUT_RECOVERY
#    NV_WRITE_RECOVERY = lib.TPM2_PT_NV_WRITE_RECOVERY
#    AUDIT_COUNTER_0 = lib.TPM2_PT_AUDIT_COUNTER_0
#    AUDIT_COUNTER_1 = lib.TPM2_PT_AUDIT_COUNTER_1


class TPM2_PT_PCR(TPM_FRIENDLY_INT):
    FIRST = lib.TPM2_PT_TPM2_PCR_FIRST
    SAVE = lib.TPM2_PT_PCR_SAVE
    EXTEND_L0 = lib.TPM2_PT_PCR_EXTEND_L0
    RESET_L0 = lib.TPM2_PT_PCR_RESET_L0
    EXTEND_L1 = lib.TPM2_PT_PCR_EXTEND_L1
    RESET_L1 = lib.TPM2_PT_PCR_RESET_L1
    EXTEND_L2 = lib.TPM2_PT_PCR_EXTEND_L2
    RESET_L2 = lib.TPM2_PT_PCR_RESET_L2
    EXTEND_L3 = lib.TPM2_PT_PCR_EXTEND_L3
    RESET_L3 = lib.TPM2_PT_PCR_RESET_L3
    EXTEND_L4 = lib.TPM2_PT_PCR_EXTEND_L4
    RESET_L4 = lib.TPM2_PT_PCR_RESET_L4
    NO_INCREMENT = lib.TPM2_PT_PCR_NO_INCREMENT
    DRTM_RESET = lib.TPM2_PT_PCR_DRTM_RESET
    POLICY = lib.TPM2_PT_PCR_POLICY
    AUTH = lib.TPM2_PT_PCR_AUTH
    LAST = lib.TPM2_PT_TPM2_PCR_LAST


class TPM2_PS(TPM_FRIENDLY_INT):
    MAIN = lib.TPM2_PS_MAIN
    PC = lib.TPM2_PS_PC
    PDA = lib.TPM2_PS_PDA
    CELL_PHONE = lib.TPM2_PS_CELL_PHONE
    SERVER = lib.TPM2_PS_SERVER
    PERIPHERAL = lib.TPM2_PS_PERIPHERAL
    TSS = lib.TPM2_PS_TSS
    STORAGE = lib.TPM2_PS_STORAGE
    AUTHENTICATION = lib.TPM2_PS_AUTHENTICATION
    EMBEDDED = lib.TPM2_PS_EMBEDDED
    HARDCOPY = lib.TPM2_PS_HARDCOPY
    INFRASTRUCTURE = lib.TPM2_PS_INFRASTRUCTURE
    VIRTUALIZATION = lib.TPM2_PS_VIRTUALIZATION
    TNC = lib.TPM2_PS_TNC
    MULTI_TENANT = lib.TPM2_PS_MULTI_TENANT
    TC = lib.TPM2_PS_TC


class TPM2_HT(TPM_FRIENDLY_INT):
    PCR = lib.TPM2_HT_PCR
    NV_INDEX = lib.TPM2_HT_NV_INDEX
    HMAC_SESSION = lib.TPM2_HT_HMAC_SESSION
    LOADED_SESSION = lib.TPM2_HT_LOADED_SESSION
    POLICY_SESSION = lib.TPM2_HT_POLICY_SESSION
    SAVED_SESSION = lib.TPM2_HT_SAVED_SESSION
    PERMANENT = lib.TPM2_HT_PERMANENT
    TRANSIENT = lib.TPM2_HT_TRANSIENT
    PERSISTENT = lib.TPM2_HT_PERSISTENT


class TPMA_SESSION(TPM_FRIENDLY_INT):
    CONTINUESESSION = lib.TPMA_SESSION_CONTINUESESSION
    AUDITEXCLUSIVE = lib.TPMA_SESSION_AUDITEXCLUSIVE
    AUDITRESET = lib.TPMA_SESSION_AUDITRESET
    DECRYPT = lib.TPMA_SESSION_DECRYPT
    ENCRYPT = lib.TPMA_SESSION_ENCRYPT
    AUDIT = lib.TPMA_SESSION_AUDIT


class TPMA_LOCALITY(TPM_FRIENDLY_INT):
    ZERO = lib.TPMA_LOCALITY_TPM2_LOC_ZERO
    ONE = lib.TPMA_LOCALITY_TPM2_LOC_ONE
    TWO = lib.TPMA_LOCALITY_TPM2_LOC_TWO
    THREE = lib.TPMA_LOCALITY_TPM2_LOC_THREE
    FOUR = lib.TPMA_LOCALITY_TPM2_LOC_FOUR
    EXTENDED_MASK = lib.TPMA_LOCALITY_EXTENDED_MASK
    EXTENDED_SHIFT = lib.TPMA_LOCALITY_EXTENDED_SHIFT


class TPM2_NT(TPM_FRIENDLY_INT):
    ORDINARY = lib.TPM2_NT_ORDINARY
    COUNTER = lib.TPM2_NT_COUNTER
    BITS = lib.TPM2_NT_BITS
    EXTEND = lib.TPM2_NT_EXTEND
    PIN_FAIL = lib.TPM2_NT_PIN_FAIL
    PIN_PASS = lib.TPM2_NT_PIN_PASS


class TPM2_HR(TPM_FRIENDLY_INT):
    HANDLE_MASK = lib.TPM2_HR_HANDLE_MASK
    RANGE_MASK = lib.TPM2_HR_RANGE_MASK
    SHIFT = lib.TPM2_HR_SHIFT
    PCR = lib.TPM2_HR_PCR
    HMAC_SESSION = lib.TPM2_HR_HMAC_SESSION
    POLICY_SESSION = lib.TPM2_HR_POLICY_SESSION
    TRANSIENT = lib.TPM2_HR_TRANSIENT
    PERSISTENT = lib.TPM2_HR_PERSISTENT
    NV_INDEX = lib.TPM2_HR_NV_INDEX
    PERMANENT = lib.TPM2_HR_PERMANENT


class TPM2_HC(TPM_FRIENDLY_INT):
    HR_HANDLE_MASK = lib.TPM2_HR_HANDLE_MASK
    HR_RANGE_MASK = lib.TPM2_HR_RANGE_MASK
    HR_SHIFT = lib.TPM2_HR_SHIFT
    HR_PCR = lib.TPM2_HR_PCR
    HR_HMAC_SESSION = lib.TPM2_HR_HMAC_SESSION
    HR_POLICY_SESSION = lib.TPM2_HR_POLICY_SESSION
    HR_TRANSIENT = lib.TPM2_HR_TRANSIENT
    HR_PERSISTENT = lib.TPM2_HR_PERSISTENT
    HR_NV_INDEX = lib.TPM2_HR_NV_INDEX
    HR_PERMANENT = lib.TPM2_HR_PERMANENT
    PCR_FIRST = lib.TPM2_PCR_FIRST
    PCR_LAST = lib.TPM2_PCR_LAST
    HMAC_SESSION_FIRST = lib.TPM2_HMAC_SESSION_FIRST
    HMAC_SESSION_LAST = lib.TPM2_HMAC_SESSION_LAST
    LOADED_SESSION_FIRST = lib.TPM2_LOADED_SESSION_FIRST
    LOADED_SESSION_LAST = lib.TPM2_LOADED_SESSION_LAST
    POLICY_SESSION_FIRST = lib.TPM2_POLICY_SESSION_FIRST
    POLICY_SESSION_LAST = lib.TPM2_POLICY_SESSION_LAST
    TRANSIENT_FIRST = lib.TPM2_TRANSIENT_FIRST
    ACTIVE_SESSION_FIRST = lib.TPM2_ACTIVE_SESSION_FIRST
    ACTIVE_SESSION_LAST = lib.TPM2_ACTIVE_SESSION_LAST
    TRANSIENT_LAST = lib.TPM2_TRANSIENT_LAST
    PERSISTENT_FIRST = lib.TPM2_PERSISTENT_FIRST
    PERSISTENT_LAST = lib.TPM2_PERSISTENT_LAST
    PLATFORM_PERSISTENT = lib.TPM2_PLATFORM_PERSISTENT
    NV_INDEX_FIRST = lib.TPM2_NV_INDEX_FIRST
    NV_INDEX_LAST = lib.TPM2_NV_INDEX_LAST
    PERMANENT_FIRST = lib.TPM2_PERMANENT_FIRST
    PERMANENT_LAST = lib.TPM2_PERMANENT_LAST


class TPM2_CLOCK(TPM_FRIENDLY_INT):
    COARSE_SLOWER = lib.TPM2_CLOCK_COARSE_SLOWER
    MEDIUM_SLOWER = lib.TPM2_CLOCK_MEDIUM_SLOWER
    FINE_SLOWER = lib.TPM2_CLOCK_FINE_SLOWER
    NO_CHANGE = lib.TPM2_CLOCK_NO_CHANGE
    FINE_FASTER = lib.TPM2_CLOCK_FINE_FASTER
    MEDIUM_FASTER = lib.TPM2_CLOCK_MEDIUM_FASTER
    COARSE_FASTER = lib.TPM2_CLOCK_COARSE_FASTER


TPM2_CLOCK_ADJUST = TPM2_CLOCK


class TPMA_NV(TPM_FRIENDLY_INTLIST):

    _FIXUP_MAP = {"NODA": "NO_DA"}

    PPWRITE = lib.TPMA_NV_PPWRITE
    OWNERWRITE = lib.TPMA_NV_OWNERWRITE
    AUTHWRITE = lib.TPMA_NV_AUTHWRITE
    POLICYWRITE = lib.TPMA_NV_POLICYWRITE
    TPM2_NT_MASK = lib.TPMA_NV_TPM2_NT_MASK
    TPM2_NT_SHIFT = lib.TPMA_NV_TPM2_NT_SHIFT
    POLICY_DELETE = lib.TPMA_NV_POLICY_DELETE
    WRITELOCKED = lib.TPMA_NV_WRITELOCKED
    WRITEALL = lib.TPMA_NV_WRITEALL
    WRITEDEFINE = lib.TPMA_NV_WRITEDEFINE
    WRITE_STCLEAR = lib.TPMA_NV_WRITE_STCLEAR
    GLOBALLOCK = lib.TPMA_NV_GLOBALLOCK
    PPREAD = lib.TPMA_NV_PPREAD
    OWNERREAD = lib.TPMA_NV_OWNERREAD
    AUTHREAD = lib.TPMA_NV_AUTHREAD
    POLICYREAD = lib.TPMA_NV_POLICYREAD
    NO_DA = lib.TPMA_NV_NO_DA
    ORDERLY = lib.TPMA_NV_ORDERLY
    CLEAR_STCLEAR = lib.TPMA_NV_CLEAR_STCLEAR
    READLOCKED = lib.TPMA_NV_READLOCKED
    WRITTEN = lib.TPMA_NV_WRITTEN
    PLATFORMCREATE = lib.TPMA_NV_PLATFORMCREATE
    READ_STCLEAR = lib.TPMA_NV_READ_STCLEAR


class TPMA_CC(TPM_FRIENDLY_INT):
    COMMANDINDEX_MASK = lib.TPMA_CC_COMMANDINDEX_MASK
    COMMANDINDEX_SHIFT = lib.TPMA_CC_COMMANDINDEX_SHIFT
    NV = lib.TPMA_CC_NV
    EXTENSIVE = lib.TPMA_CC_EXTENSIVE
    FLUSHED = lib.TPMA_CC_FLUSHED
    CHANDLES_MASK = lib.TPMA_CC_CHANDLES_MASK
    CHANDLES_SHIFT = lib.TPMA_CC_CHANDLES_SHIFT
    RHANDLE = lib.TPMA_CC_RHANDLE
    V = lib.TPMA_CC_V
    RES_MASK = lib.TPMA_CC_RES_MASK
    RES_SHIFT = lib.TPMA_CC_RES_SHIFT


class TPMA_OBJECT(TPM_FRIENDLY_INTLIST):
    FIXEDTPM = lib.TPMA_OBJECT_FIXEDTPM
    STCLEAR = lib.TPMA_OBJECT_STCLEAR
    FIXEDPARENT = lib.TPMA_OBJECT_FIXEDPARENT
    SENSITIVEDATAORIGIN = lib.TPMA_OBJECT_SENSITIVEDATAORIGIN
    USERWITHAUTH = lib.TPMA_OBJECT_USERWITHAUTH
    ADMINWITHPOLICY = lib.TPMA_OBJECT_ADMINWITHPOLICY
    NODA = lib.TPMA_OBJECT_NODA
    ENCRYPTEDDUPLICATION = lib.TPMA_OBJECT_ENCRYPTEDDUPLICATION
    RESTRICTED = lib.TPMA_OBJECT_RESTRICTED
    DECRYPT = lib.TPMA_OBJECT_DECRYPT
    SIGN_ENCRYPT = lib.TPMA_OBJECT_SIGN_ENCRYPT

    DEFAULT_TPM2_TOOLS_CREATE_ATTRS = (
        lib.TPMA_OBJECT_DECRYPT
        | lib.TPMA_OBJECT_SIGN_ENCRYPT
        | lib.TPMA_OBJECT_FIXEDTPM
        | lib.TPMA_OBJECT_FIXEDPARENT
        | lib.TPMA_OBJECT_SENSITIVEDATAORIGIN
        | lib.TPMA_OBJECT_USERWITHAUTH
    )

    DEFAULT_TPM2_TOOLS_CREATEPRIMARY_ATTRS = (
        lib.TPMA_OBJECT_RESTRICTED
        | lib.TPMA_OBJECT_DECRYPT
        | lib.TPMA_OBJECT_FIXEDTPM
        | lib.TPMA_OBJECT_FIXEDPARENT
        | lib.TPMA_OBJECT_SENSITIVEDATAORIGIN
        | lib.TPMA_OBJECT_USERWITHAUTH
    )

    _FIXUP_MAP = {
        "SIGN": "SIGN_ENCRYPT",
        "ENCRYPT": "SIGN_ENCRYPT",
    }


class TPMA_ALGORITHM(TPM_FRIENDLY_INT):
    ASYMMETRIC = lib.TPMA_ALGORITHM_ASYMMETRIC
    SYMMETRIC = lib.TPMA_ALGORITHM_SYMMETRIC
    HASH = lib.TPMA_ALGORITHM_HASH
    OBJECT = lib.TPMA_ALGORITHM_OBJECT
    SIGNING = lib.TPMA_ALGORITHM_SIGNING
    ENCRYPTING = lib.TPMA_ALGORITHM_ENCRYPTING
    METHOD = lib.TPMA_ALGORITHM_METHOD


class TPMA_PERMANENT(TPM_FRIENDLY_INT):
    OWNERAUTHSET = lib.TPMA_PERMANENT_OWNERAUTHSET
    ENDORSEMENTAUTHSET = lib.TPMA_PERMANENT_ENDORSEMENTAUTHSET
    LOCKOUTAUTHSET = lib.TPMA_PERMANENT_LOCKOUTAUTHSET
    DISABLECLEAR = lib.TPMA_PERMANENT_DISABLECLEAR
    INLOCKOUT = lib.TPMA_PERMANENT_INLOCKOUT
    TPMGENERATEDEPS = lib.TPMA_PERMANENT_TPMGENERATEDEPS


class TPMA_STARTUP(TPM_FRIENDLY_INT):
    CLEAR_PHENABLE = lib.TPMA_STARTUP_CLEAR_PHENABLE
    CLEAR_SHENABLE = lib.TPMA_STARTUP_CLEAR_SHENABLE
    CLEAR_EHENABLE = lib.TPMA_STARTUP_CLEAR_EHENABLE
    CLEAR_PHENABLENV = lib.TPMA_STARTUP_CLEAR_PHENABLENV
    CLEAR_ORDERLY = lib.TPMA_STARTUP_CLEAR_ORDERLY


class TPMA_MEMORY(TPM_FRIENDLY_INT):
    SHAREDRAM = lib.TPMA_MEMORY_SHAREDRAM
    SHAREDNV = lib.TPMA_MEMORY_SHAREDNV
    OBJECTCOPIEDTORAM = lib.TPMA_MEMORY_OBJECTCOPIEDTORAM


class TPM_OBJECT(object):
    def __init__(self, _cdata=None, **kwargs):

        if _cdata is None:
            _cdata = ffi.new(f"{self.__class__.__name__} *")

        self._cdata = _cdata

        tipe = ffi.typeof(_cdata)
        if tipe.kind == "pointer":
            tipe = tipe.item

        expected_cname = self._fixup_classname(tipe)
        if expected_cname != self.__class__.__name__:
            raise TypeError(
                f"Unexpected _cdata type {expected_cname}, expected {self.__class__.__name__}"
            )
        fields = [x[0] for x in tipe.fields]
        for k, v in kwargs.items():
            if k not in fields:
                raise AttributeError(
                    f"{self.__class__.__name__} has no field by the name of {k}"
                )
            self.__setattr__(k, v)

    @staticmethod
    def _fixup_classname(tipe):
        # Some versions of tpm2-tss had anonymous structs, so the kind will be struct
        # but the name will not contain it
        if tipe.cname.startswith(tipe.kind):
            return tipe.cname[len(tipe.kind) + 1 :]

        return tipe.cname

    def __getattribute__(self, key):
        try:
            # go through object to avoid invoking THIS objects __getattribute__ call
            # and thus infinite recursion
            return object.__getattribute__(self, key)
        except AttributeError:
            # Ok the object has no idea what you're looking for... can we handle it?
            # Yes we could use self._cdata as it will only recurse once, but lets avoid it.
            _cdata = object.__getattribute__(self, "_cdata")

            # Get the attribute they're looking for out of _cdata
            x = getattr(_cdata, key)

            # type is reserved by python, so use tipe
            tipe = None
            try:
                tipe = ffi.typeof(x)
            except TypeError:
                # Python native values wont ffi.typeof
                return x

            # Native arrays, like uint8_t[4] we don't wrap. We just let the underlying
            # data type handle it.
            if tipe.kind == "array" and tipe.cname.startswith("uint"):
                return x

            # if it's not a struct or union, we don't wrap it and thus we don't
            # know what to do with it.
            if tipe.kind != "struct" and tipe.kind != "union":
                raise TypeError(f'Not struct or union, got: "{tipe.kind}"')

            clsname = TPM_OBJECT._fixup_classname(tipe)
            subclass = globals()[clsname]
            obj = subclass(_cdata=x)
            return obj

    def __setattr__(self, key, value):
        # print(f"SET ATTRIBUTE {key}")
        try:
            # Get _cdata without invoking getattr
            _cdata = object.__getattribute__(self, "_cdata")
            setattr(_cdata, key, value)
        except (AttributeError, TypeError):
            return object.__setattr__(self, key, value)


class TPML_OBJECT(TPM_OBJECT):
    def __getattribute__(self, key):

        try:
            # Can the parent handle it?
            x = TPM_OBJECT.__getattribute__(self, key)
            return x
        except TypeError:
            pass

        # Must be a TPML style array
        # Get cdata without implicitly invoking a derived classes __getattribute__
        # This will prevent recursion and stack depth issues.
        _cdata = object.__getattribute__(self, "_cdata")

        # This will invoke the CFFI implementation, so getattr is safe here.
        x = getattr(_cdata, key)

        # If this isn't a CFFI type, something wen't crazy, and typeof() will raise TypeError.
        tipe = ffi.typeof(x)
        if tipe.kind != "array":
            raise TypeError(
                f'Unknown scalar conversion for kind "{tipe.kind}" for key "{key}"'
            )

        # subclasses in the arrays within the CTypes are fixed, so
        # we only need to do this once
        clsname = TPM_OBJECT._fixup_classname(tipe.item)
        subclass = globals()[clsname]

        l = []
        # do not go through __len__
        count = _cdata.count
        for i in range(0, count):
            obj = subclass(_cdata=x[i])
            l.append(obj)

        return l

    def __len__(self):

        return self._cdata.count


class TPMU_PUBLIC_PARMS(TPM_OBJECT):
    pass


class TPMT_PUBLIC(TPM_OBJECT):
    pass


class TPM2B_ATTEST(TPM_OBJECT):
    pass


class TPM2B_CONTEXT_DATA(TPM_OBJECT):
    pass


class TPM2B_CONTEXT_SENSITIVE(TPM_OBJECT):
    pass


class TPM2B_CREATION_DATA(TPM_OBJECT):
    pass


class TPM2B_DATA(TPM_OBJECT):
    pass


class TPM2B_DIGEST(TPM_OBJECT):
    pass


class TPM2B_ECC_PARAMETER(TPM_OBJECT):
    pass


class TPM2B_ECC_POINT(TPM_OBJECT):
    pass


class TPM2B_ENCRYPTED_SECRET(TPM_OBJECT):
    pass


class TPM2B_EVENT(TPM_OBJECT):
    pass


class TPM2B_ID_OBJECT(TPM_OBJECT):
    pass


class TPM2B_IV(TPM_OBJECT):
    pass


class TPM2B_MAX_BUFFER(TPM_OBJECT):
    pass


class TPM2B_MAX_NV_BUFFER(TPM_OBJECT):
    pass


class TPM2B_NAME(TPM_OBJECT):
    pass


class TPM2B_NV_PUBLIC(TPM_OBJECT):
    pass


class TPM2B_PRIVATE(TPM_OBJECT):
    pass


class TPM2B_PRIVATE_KEY_RSA(TPM_OBJECT):
    pass


class TPM2B_PRIVATE_VENDOR_SPECIFIC(TPM_OBJECT):
    pass


class TPM2B_PUBLIC(TPM_OBJECT):
    pass


class TPM2B_PUBLIC_KEY_RSA(TPM_OBJECT):
    pass


class TPM2B_SENSITIVE(TPM_OBJECT):
    pass


class TPM2B_SENSITIVE_CREATE(TPM_OBJECT):
    pass


class TPM2B_SENSITIVE_DATA(TPM_OBJECT):
    pass


class TPM2B_SYM_KEY(TPM_OBJECT):
    pass


class TPM2B_TEMPLATE(TPM_OBJECT):
    pass


class TPML_AC_CAPABILITIES(TPM_OBJECT):
    pass


class TPML_ALG(TPM_OBJECT):
    pass


class TPML_ALG_PROPERTY(TPM_OBJECT):
    pass


class TPML_CC(TPM_OBJECT):
    pass


class TPML_CCA(TPM_OBJECT):
    pass


class TPML_DIGEST(TPML_OBJECT):
    def __getitem__(self, item):
        try:
            return object.__getitem__(self, item)
        except AttributeError:
            if isinstance(item, slice):
                if item.stop is None:
                    item = slice(item.start, len(self) - 1, item.step)
                digest_list = self._cdata.digests[item]
                return [TPM2B_unpack(x) for x in digest_list]

            return TPM2B_unpack(self._cdata.digests[item])


class TPML_DIGEST_VALUES(TPML_OBJECT):
    pass


class TPML_ECC_CURVE(TPML_OBJECT):
    pass


class TPML_HANDLE(TPML_OBJECT):
    pass


class TPML_INTEL_PTT_PROPERTY(TPML_OBJECT):
    pass


class TPML_PCR_SELECTION(TPML_OBJECT):
    def __init__(self, pcr_selections=None, _cdata=None):
        super().__init__(_cdata=_cdata)

        if pcr_selections is None or len(pcr_selections) == 0:
            return

        if len(pcr_selections) > lib.TPM2_NUM_PCR_BANKS:
            raise RuntimeError(
                f"PCR Selection list greater than {lib.TPM2_NUM_PCR_BANKS}, "
                f"got {len(pcr_selections)}"
            )

        self._cdata.count = len(pcr_selections)
        for i, p in enumerate(pcr_selections):
            self._cdata.pcrSelections[i] = p._cdata[0]

    @staticmethod
    def parse(selections):

        if selections is None or len(selections) == 0:
            return TPML_PCR_SELECTION()

        selectors = selections.split("+") if "+" in selections else [selections]

        if len(selectors) - 1 != selections.count("+"):
            raise RuntimeError(
                f"Malformed PCR bank selection list (unbalanced +), got: {selections}"
            )

        for x in selectors:
            if len(x) == 0:
                raise RuntimeError(
                    f"Malformed PCR bank selection list (unbalanced +), got: {selections}"
                )

        count = len(selectors)
        if count > lib.TPM2_NUM_PCR_BANKS:
            raise RuntimeError(
                f"PCR Selection list greater than f{lib.TPM2_NUM_PCR_BANKS}, "
                f"got {len(selectors)}"
            )

        selections = [TPMS_PCR_SELECTION.parse(x) for x in selectors]

        return TPML_PCR_SELECTION(selections)


class TPML_TAGGED_PCR_PROPERTY(TPML_OBJECT):
    pass


class TPML_TAGGED_TPM_PROPERTY(TPML_OBJECT):
    pass


class TPMS_AC_OUTPUT(TPM_OBJECT):
    pass


class TPMS_ALGORITHM_DESCRIPTION(TPM_OBJECT):
    pass


class TPMS_ALGORITHM_DETAIL_ECC(TPM_OBJECT):
    pass


class TPMS_ALG_PROPERTY(TPM_OBJECT):
    pass


class TPMS_ASYM_PARMS(TPM_OBJECT):
    pass


class TPMS_ATTEST(TPM_OBJECT):
    pass


class TPMS_AUTH_COMMAND(TPM_OBJECT):
    pass


class TPMS_AUTH_RESPONSE(TPM_OBJECT):
    pass


class TPMS_CAPABILITY_DATA(TPM_OBJECT):
    pass


class TPMS_CERTIFY_INFO(TPM_OBJECT):
    pass


class TPMS_CLOCK_INFO(TPM_OBJECT):
    pass


class TPMS_COMMAND_AUDIT_INFO(TPM_OBJECT):
    pass


class TPMS_CONTEXT(TPM_OBJECT):
    pass


class TPMS_CONTEXT_DATA(TPM_OBJECT):
    pass


class TPMS_CREATION_DATA(TPM_OBJECT):
    pass


class TPMS_CREATION_INFO(TPM_OBJECT):
    pass


class TPMS_ECC_PARMS(TPM_OBJECT):
    pass


class TPMS_ECC_POINT(TPM_OBJECT):
    pass


class TPMS_EMPTY(TPM_OBJECT):
    pass


class TPMS_ID_OBJECT(TPM_OBJECT):
    pass


class TPMS_KEYEDHASH_PARMS(TPM_OBJECT):
    pass


class TPMS_NV_CERTIFY_INFO(TPM_OBJECT):
    pass


class TPMS_NV_PIN_COUNTER_PARAMETERS(TPM_OBJECT):
    pass


class TPMS_NV_PUBLIC(TPM_OBJECT):
    pass


class TPMS_PCR_SELECT(TPM_OBJECT):
    pass


class TPMS_PCR_SELECTION(TPM_OBJECT):
    def __init__(self, halg=0, pcrs=None, _cdata=None):
        super().__init__(_cdata=_cdata)

        if not halg and not pcrs:
            return

        if bool(halg) != bool(pcrs):
            raise RuntimeError("halg and pcrs MUST be specified")

        self._cdata.hash = halg
        self._cdata.sizeofSelect = 3

        if pcrs == "all" or (len(pcrs) == 1 and pcrs[0] == "all"):
            self._cdata.pcrSelect[0] = 0xFF
            self._cdata.pcrSelect[1] = 0xFF
            self._cdata.pcrSelect[2] = 0xFF
            return

        for pcr in pcrs:
            if pcr < 0 or pcr > lib.TPM2_PCR_LAST:
                raise RuntimeError(f"PCR Index out of range, got {pcr}")
            self._cdata.pcrSelect[pcr // 8] |= 1 << (pcr % 8)

    @staticmethod
    def parse(selection):

        if selection is None or len(selection) == 0:
            return TPMS_PCR_SELECTION()

        hunks = [x.strip() for x in selection.split(":")]
        if len(hunks) != 2:
            raise RuntimeError(f"PCR Selection malformed, got {selection}")

        try:
            halg = int(hunks[0], 0)
        except ValueError:
            try:
                halg = TPM2_ALG.parse(hunks[0])
            except KeyError:
                raise RuntimeError(
                    f"Expected int or algorithm friendly name, got {hunks[0]}"
                )

        if hunks[1] != "all":
            try:
                pcrs = [int(x.strip(), 0) for x in hunks[1].split(",")]
            except ValueError:
                raise RuntimeError(f"Expected PCR number, got {hunks[1]}")
        else:
            pcrs = hunks[1]

        return TPMS_PCR_SELECTION(halg=halg, pcrs=pcrs)


class TPMS_QUOTE_INFO(TPM_OBJECT):
    pass


class TPMS_RSA_PARMS(TPM_OBJECT):
    pass


class TPMS_SCHEME_ECDAA(TPM_OBJECT):
    pass


class TPMS_SCHEME_HASH(TPM_OBJECT):
    pass


class TPMS_SCHEME_XOR(TPM_OBJECT):
    pass


class TPMS_SENSITIVE_CREATE(TPM_OBJECT):
    pass


class TPMS_SESSION_AUDIT_INFO(TPM_OBJECT):
    pass


class TPMS_SIGNATURE_ECC(TPM_OBJECT):
    pass


class TPMS_SIGNATURE_RSA(TPM_OBJECT):
    pass


class TPMS_SYMCIPHER_PARMS(TPM_OBJECT):
    pass


class TPMS_TAGGED_PCR_SELECT(TPM_OBJECT):
    pass


class TPMS_TAGGED_PROPERTY(TPM_OBJECT):
    pass


class TPMS_TIME_ATTEST_INFO(TPM_OBJECT):
    pass


class TPMS_TIME_INFO(TPM_OBJECT):
    pass


class TPMT_ECC_SCHEME(TPM_OBJECT):
    pass


class TPMU_ASYM_SCHEME(TPM_OBJECT):
    pass


class TPMT_SYM_DEF_OBJECT(TPM_OBJECT):
    pass


class TPMT_KDF_SCHEME(TPM_OBJECT):
    pass


class TPMT_TK_CREATION(TPM_OBJECT):
    pass


class TPMT_ASYM_SCHEME(TPM_OBJECT):
    pass