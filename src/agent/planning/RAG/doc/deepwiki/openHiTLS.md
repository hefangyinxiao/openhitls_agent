# Overview

Relevant source files

  * [CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/CMakeLists.txt)
  * [bsl/log/src/log.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/log/src/log.c)
  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [configure.py](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py)
  * [crypto/drbg/include/crypt_drbg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/include/crypt_drbg.h)
  * [crypto/eal/src/eal_md.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c)
  * [crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
  * [docs/en/5_Developer Guide/4_provider Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md)
  * [docs/index/index.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/index/index.md)
  * [include/bsl/bsl_log.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/bsl/bsl_log.h)
  * [include/crypto/crypt_eal_rand.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_rand.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/demo/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt)
  * [testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
  * [testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c)
  * [testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)
  * [testcode/demo/privpass_token.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c)
  * [testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
  * [testcode/demo/sm2enc.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c)
  * [testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)

openHiTLS is a comprehensive Transport Layer Security (TLS) library that
provides a secure communication framework for applications. It implements
multiple TLS protocol versions, an extensive suite of cryptographic
algorithms, and a flexible provider architecture that allows for customization
and extensibility.

This overview introduces the main components and architecture of openHiTLS,
highlighting its layered design, key features, and fundamental concepts. For
more specific information about using the library, see [Getting
Started](/openHiTLS/openHiTLS/1.2-getting-started), and for architectural
details, see [Architecture](/openHiTLS/openHiTLS/2-architecture).

## Key Components

openHiTLS is structured as a layered system with several main components:

    
    
    Basic Support Layer (BSL)
    
    Applications
    
    TLS Protocol Layer
    
    Cryptographic Services Layer
    
    Provider Framework
    
    Logging
    
    Memory Management
    
    OS Abstraction
    
    I/O Handling
    
    ASN.1/PEM Encoding
    
    PKI/X.509
    
    Default Provider
    
    Custom Providers

Sources:
[config/json/feature.json1-630](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L1-L630)
[crypto/eal/src/eal_rand.c1-963](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L1-L963)
[docs/en/5_Developer Guide/4_provider Development
Guide.md1-512](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L1-L512)

### TLS Protocol Layer

The TLS Protocol Layer handles TLS handshakes, secure data transmission, and
session management. It supports multiple protocol versions including TLS 1.2,
TLS 1.3, and DTLS 1.2.

    
    
    TLS Protocol Layer
    
    Handshake Protocol
    
    Record Protocol
    
    Alert Protocol
    
    Configuration
    
    ClientHello/ServerHello
    
    Key Exchange
    
    Certificate Verification
    
    Extensions Handling
    
    Record Writing
    
    Record Reading
    
    Encryption/Decryption
    
    Protocol Versions
    
    Cipher Suites
    
    Key Exchange Groups
    
    Signature Algorithms

Sources:
[config/json/feature.json222-583](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L222-L583)
[tls/include/tls.h1-30](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h#L1-L30)
[tls/handshake/common/include/hs_msg.h1-40](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h#L1-L40)

### Cryptographic Services Layer

The Cryptographic Services Layer provides a unified interface for
cryptographic operations, abstracting away differences between algorithm
implementations. It supports a wide range of cryptographic primitives:

    
    
    Cryptographic Services Layer
    
    EAL Interface
    
    Symmetric Encryption
    
    Asymmetric Cryptography
    
    Hash Functions
    
    MAC Functions
    
    Random Number Generation
    
    Key Derivation
    
    AES
    
    SM4
    
    ChaCha20
    
    RSA
    
    ECC/ECDSA
    
    SM2
    
    Ed25519/X25519
    
    Hybrid KEM
    
    Post-Quantum
    
    SHA1/2/3
    
    SM3
    
    MD5
    
    DRBG
    
    HKDF
    
    PBKDF2
    
    SCRYPT

Sources:
[config/json/feature.json40-220](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L40-L220)
[crypto/eal/src/eal_rand.c1-963](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L1-L963)
[crypto/eal/src/eal_md.c1-75](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c#L1-L75)

### Provider Framework

The Provider Framework enables the dynamic loading and management of
cryptographic implementations. It supports both built-in and custom providers,
offering flexibility to applications with specific security requirements.

    
    
    Provider Framework
    
    Provider Manager
    
    Provider Loading/Unloading
    
    Algorithm Discovery
    
    Provider Selection
    
    Default Provider
    
    Dynamic Loading
    
    Algorithm Capabilities Query
    
    Scoring/Prioritization
    
    Default Implementations
    
    Custom Implementations
    
    Hardware-optimized Implementations
    
    Generic Implementations

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md1-512](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L1-L512)
[crypto/eal/src/eal_rand.c688-788](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L688-L788)

### Basic Support Layer (BSL)

The Basic Support Layer provides fundamental services required by the higher
layers:

  * **Logging** : For diagnostics and debugging
  * **Memory Management** : Allocation and tracking
  * **OS Abstraction** : Platform independence
  * **I/O Handling** : Network and file operations
  * **ASN.1/PEM Encoding** : Certificate and key format handling

Sources:
[config/json/feature.json2-39](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L2-L39)
[include/bsl/bsl_log.h1-26](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/bsl/bsl_log.h#L1-L26)

## Random Number Generation

Secure random number generation is crucial for cryptographic operations.
openHiTLS implements a robust DRBG (Deterministic Random Bit Generator)
system:

    
    
    CRYPT_EAL_RandInit
    
    EAL_RandNewDrbg
    
    Initialize Entropy Source
    
    Create DRBG Context
    
    Instantiate DRBG
    
    CRYPT_EAL_Randbytes
    
    CRYPT_EAL_RandbytesWithAdin
    
    EAL_DrbgbytesWithAdin
    
    Generate Random Bytes
    
    CRYPT_EAL_RandSeed
    
    EAL_DrbgSeedWithAdin
    
    Reseed DRBG

Sources:
[crypto/eal/src/eal_rand.c51-687](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L51-L687)
[testcode/demo/drbg.c1-109](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c#L1-L109)

## Library Usage Flow

The typical usage flow of openHiTLS involves several steps:

    
    
    Data TransferConnectionI/O SetupTLS ContextConfigurationInitializationApplicationData TransferConnectionI/O SetupTLS ContextConfigurationInitializationApplicationBSL_SAL_CallBack_CtrlBSL_ERR_InitCRYPT_EAL_InitCRYPT_EAL_ProviderRandInitCtxHITLS_CFG_NewTLS12ConfigLoad Certificates and KeysHITLS_NewBSL_UIO_NewBSL_UIO_CtrlHITLS_SetUioHITLS_Connect/HITLS_AcceptHITLS_WriteHITLS_ReadProcess DataHITLS_CloseHITLS_FreeHITLS_CFG_FreeConfig

Sources:
[testcode/demo/client.c1-171](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L1-L171)
[testcode/demo/server.c1-187](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L1-L187)

## Supported Features

openHiTLS supports a rich set of features, including:

Feature Category| Supported Implementations  
---|---  
TLS Versions| TLS 1.2, TLS 1.3, DTLS 1.2, TLCP 1.1  
Hash Functions| SHA-1, SHA-2, SHA-3, SM3, MD5  
Symmetric Encryption| AES, SM4, ChaCha20  
Asymmetric Cryptography| RSA, ECC/ECDSA, SM2, Ed25519/X25519, Post-Quantum
algorithms  
Key Exchange| ECDHE, DHE, PSK, KEM  
MAC Functions| HMAC, CMAC, GMAC, CBC-MAC, SipHash  
Certificate Handling| X.509, PKCS#12, Certificate Validation  
  
Sources:
[config/json/feature.json40-583](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L40-L583)
[testcode/demo/sm2sign.c1-118](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c#L1-L118)
[testcode/demo/sm2enc.c1-113](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c#L1-L113)
[testcode/demo/ecdh.c1-140](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c#L1-L140)

## Build and Configuration System

openHiTLS uses a flexible build system based on Python and CMake:

    
    
    configure.py
    
    Parse Arguments
    
    Update Configurations
    
    Generate modules.cmake
    
    CMake Build Process
    
    feature.json
    
    compile.json
    
    Feature Selections
    
    Compiler Options
    
    Assembly Optimizations
    
    Compiled Libraries
    
    Test Executables

The configuration system allows customization of:

  * Enabled features and algorithms
  * Assembly optimizations for specific architectures
  * Compiler and linker options
  * Library output types (static/shared/object)

Sources:
[configure.py1-135](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L1-L135)
[testcode/demo/CMakeLists.txt1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt#L1-L53)
[testcode/sdv/CMakeLists.txt1-200](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt#L1-L200)

## Sample Applications

openHiTLS includes sample applications demonstrating key functionality:

  1. **TLS Client/Server** : Simple client and server implementation using TLS
  2. **Cryptographic Operations** : Examples of various cryptographic operations: 
     * Random number generation (DRBG)
     * Key exchange (ECDH)
     * Digital signatures (SM2Sign)
     * Encryption/decryption (SM4CBC, SM2Enc)
     * Key derivation (PBKDF2)
     * Hashing

These examples serve as a starting point for developers integrating openHiTLS
into their applications.

Sources:
[testcode/demo/client.c1-171](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L1-L171)
[testcode/demo/server.c1-187](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L1-L187)
[testcode/demo/privpass_token.c1-315](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c#L1-L315)

## Error Handling

openHiTLS implements a comprehensive error handling system with detailed error
codes for different modules:

  * TLS Protocol errors (HITLS_ERR_TLS)
  * System call errors (HITLS_ERR_SYSCALL)
  * Connection state indicators (HITLS_WANT_* codes)
  * Specific error codes for various components

Applications can use these error codes to diagnose issues and take appropriate
actions.

Sources:
[include/tls/hitls_error.h1-169](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L1-L169)

## Summary

openHiTLS provides a comprehensive, flexible, and extensible security
framework for applications requiring TLS communication. Its layered
architecture, extensive algorithm support, and provider framework make it
suitable for a wide range of use cases, from standard web applications to
specialized security-sensitive environments.

The library's modular design allows for customization and extension to meet
specific security requirements, while the optimized implementations ensure
high performance across different platforms.

# Key Features

Relevant source files

  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)
  * [crypto/hpke/src/hpke.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c)
  * [crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)
  * [crypto/provider/src/default/crypt_default_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c)
  * [docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md)
  * [include/crypto/crypt_eal_hpke.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_hpke.h)
  * [include/crypto/crypt_eal_init.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h)
  * [include/tls/hitls_crypt_type.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_crypt_type.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/framework/include/helper.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/include/helper.h)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.c)
  * [testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.data)
  * [testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c)
  * [tls/config/src/config_group.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c)
  * [tls/crypt/crypt_adapt/crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_adapt/crypt.c)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_ctx.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_ctx.h)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/common/src/hs_kx.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
  * [tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)
  * [tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)

This page provides a comprehensive overview of the key features available in
openHiTLS, a high-performance, security-focused TLS library. It covers the
supported cryptographic algorithms, TLS protocol versions, and major
capabilities that make openHiTLS suitable for various security-critical
applications.

## Architecture Overview

openHiTLS is built on a layered architecture that separates concerns and
enables flexibility, security, and performance.

    
    
    Basic Support Layer (BSL)
    
    Applications
    
    TLS Protocol Layer
    
    Cryptographic Services Layer
    
    Provider Framework
    
    Logging
    
    Memory Management
    
    OS Abstraction
    
    I/O Handling
    
    ASN.1/PEM Encoding
    
    PKI/X.509
    
    Default Provider
    
    Custom Providers

Sources:
[config/json/feature.json1-631](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L1-L631)
[crypto/provider/src/default/crypt_default_provider.c1-199](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L1-L199)

## Cryptographic Algorithms

openHiTLS provides a comprehensive suite of cryptographic algorithms,
including traditional, national-standard, and post-quantum algorithms.

### Hash Functions

Algorithm| Description  
---|---  
MD5| Legacy hash function (128-bit)  
SHA-1| Legacy hash function (160-bit)  
SHA-2| Family including SHA-224, SHA-256, SHA-384, SHA-512  
SHA-3| Modern hash function family with different output sizes  
SM3| Chinese cryptographic standard  
  
### Symmetric Encryption

Algorithm| Modes| Key Sizes  
---|---|---  
AES| CBC, GCM, CCM, ECB, XTS, CTR, OFB, CFB| 128, 192, 256 bits  
SM4| CBC, GCM, ECB, XTS, CTR, OFB, CFB| 128 bits  
ChaCha20| ChaCha20-Poly1305| 256 bits  
  
### Public Key Cryptography

    
    
    Public Key Cryptography
    
    Key Exchange
    
    Digital Signatures
    
    Encryption/Decryption
    
    Post-Quantum
    
    RSA
    
    DH
    
    ECDH
    
    X25519
    
    SM2
    
    RSA
    
    ECDSA
    
    DSA
    
    Ed25519
    
    SM2
    
    RSA
    
    SM2
    
    PAILLIER
    
    ELGAMAL
    
    MLKEM
    
    SLH-DSA
    
    ML-DSA
    
    HYBRID KEM

Sources:
[config/json/feature.json40-170](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L40-L170)
[config/macro_config/hitls_config_layer_crypto.h231-262](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L231-L262)
[crypto/provider/src/default/crypt_default_provider.c40-108](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L40-L108)

### Key Derivation and Random Number Generation

Category| Algorithms  
---|---  
KDF| HKDF, PBKDF2, SCRYPT, TLS 1.2 KDF  
MAC| HMAC, GMAC, CMAC, CBC-MAC, SIPHASH  
DRBG| Hash-based, HMAC-based, CTR-based  
  
### Hybrid Public Key Encryption (HPKE)

openHiTLS implements HPKE as defined in RFC 9180, which provides a framework
for combining asymmetric and symmetric cryptography for secure data
transmission.

    
    
    HPKE
    
    Key Encapsulation Mechanisms (KEM)
    
    Key Derivation Functions (KDF)
    
    Authenticated Encryption with Associated Data (AEAD)
    
    DHKEM(P-256, HKDF-SHA256)
    
    DHKEM(P-384, HKDF-SHA384)
    
    DHKEM(P-521, HKDF-SHA512)
    
    DHKEM(X25519, HKDF-SHA256)
    
    HKDF-SHA256
    
    HKDF-SHA384
    
    HKDF-SHA512
    
    AES-128-GCM
    
    AES-256-GCM
    
    ChaCha20Poly1305
    
    Export-only

Sources:
[crypto/hpke/src/hpke.c108-126](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c#L108-L126)
[testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.c1-210](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.c#L1-L210)

## Protocol Support

openHiTLS supports multiple TLS protocol versions and their variants, making
it suitable for a wide range of use cases.

### Supported Protocols

Protocol| Description  
---|---  
TLS 1.2| Standard TLS version widely deployed  
TLS 1.3| Latest TLS version with improved security and performance  
TLCP 1.1| Chinese cryptographic protocol standard  
DTLS 1.2| Datagram TLS for UDP-based applications  
  
### Cipher Suites

openHiTLS supports numerous cipher suites for different protocol versions,
including:

  * TLS 1.3 suites (AES-GCM, AES-CCM, ChaCha20-Poly1305)
  * TLS 1.2 suites with various key exchange methods (RSA, DHE, ECDHE)
  * TLCP cipher suites (SM4-CBC-SM3)
  * PSK-based cipher suites

Sources:
[config/json/feature.json222-556](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L222-L556)
[tls/handshake/common/src/hs_kx.c1-170](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L1-L170)

### Protocol Extensions

    
    
    TLS Extensions
    
    Security Extensions
    
    Functionality Extensions
    
    Performance Extensions
    
    Extended Master Secret
    
    Signature Algorithms
    
    Renegotiation Info
    
    Key Share
    
    Server Name Indication (SNI)
    
    Application Layer Protocol Negotiation (ALPN)
    
    Supported Groups
    
    Certificate Status Request
    
    Custom Extensions
    
    Session Tickets
    
    Pre-Shared Key (PSK)
    
    Early Data
    
    Record Size Limit

Sources:
[tls/handshake/pack/src/pack_extensions.c119-500](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L119-L500)
[tls/handshake/recv/src/recv_server_hello.c1-35](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c#L1-L35)

## Provider Framework

The provider framework enables pluggable implementations of cryptographic
algorithms, allowing for customization, optimization, and regulatory
compliance.

    
    
    Provider Framework
    
    Provider Manager
    
    Default Provider
    
    Custom Providers
    
    Generic Implementations
    
    Hardware-optimized Implementations
    
    External Vendor Implementations
    
    HSM Integrations
    
    Custom Optimized Implementations
    
    Software AES
    
    Software SHA-2
    
    AES-NI
    
    AVX2 Optimizations
    
    ARM Crypto Extensions

The provider framework allows for:

  1. **Algorithm Discovery** : Runtime discovery of supported algorithms
  2. **Algorithm Selection** : Selection of the most appropriate implementation
  3. **Hardware Acceleration** : Automatic use of hardware-accelerated implementations when available
  4. **Custom Implementations** : Integration of custom or third-party implementations

Sources:
[crypto/provider/include/crypt_provider.h1-29](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h#L1-L29)
[crypto/provider/src/default/crypt_default_provider.c191-199](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L191-L199)

## Performance Optimizations

openHiTLS includes various performance optimizations to ensure high throughput
and low latency:

  1. **Assembly Optimizations** : Hand-optimized assembly code for critical cryptographic operations on multiple architectures:

     * x86-64 (including AVX512 extensions)
     * ARMv8 (including Crypto Extensions)
  2. **Efficient Memory Management** : Customized memory allocation and management for cryptographic operations

  3. **Configurable Features** : Ability to include only required features to minimize footprint

Sources:
[config/json/feature.json194-218](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L194-L218)
[testcode/framework/tls/CMakeLists.txt1-109](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt#L1-L109)

## Building and Integration

openHiTLS provides flexible build options for various environments and use
cases:

  1. **CMake-based Build System** : Modern build system with extensive configuration options

  2. **Feature Selection** : Granular control over which features to include:
         
         ./configure.py --enable-tls13 --enable-asm
         

  3. **Cross-Platform Support** : Builds on various operating systems and architectures

  4. **Test Framework** : Comprehensive testing infrastructure for validating functionality and performance

Sources:
[testcode/sdv/CMakeLists.txt1-235](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt#L1-L235)
[config/macro_config/hitls_config_layer_crypto.h1-43](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L1-L43)

## Error Handling

openHiTLS includes a comprehensive error handling system that provides
detailed information about errors that occur during operation:

  1. **Hierarchical Error Codes** : Error codes are organized by module and severity
  2. **Detailed Error Messages** : Clear error messages for debugging
  3. **Error Propagation** : Consistent error propagation throughout the library

Sources:
[include/tls/hitls_error.h32-450](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L32-L450)
[tls/include/tls_binlog_id.h33-60](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h#L33-L60)

## Security Features

  * **State-of-the-art Cryptography** : Support for the latest cryptographic algorithms and protocols
  * **Side-Channel Resistance** : Implementations designed to resist various side-channel attacks
  * **Post-Quantum Readiness** : Support for post-quantum and hybrid cryptographic algorithms
  * **Secure Defaults** : Secure configuration defaults to prevent common misconfigurations
  * **Comprehensive Certificate Validation** : Robust X.509 certificate validation

Sources:
[tls/handshake/common/src/hs_kx.c260-299](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L260-L299)
[include/tls/hitls_crypt_type.h97-106](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_crypt_type.h#L97-L106)

# Getting Started

Relevant source files

  * [.github/workflows/cmake-single-platform.yml](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-single-platform.yml)
  * [CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/CMakeLists.txt)
  * [README-zh.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README-zh.md)
  * [README.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md)
  * [bsl/log/src/log.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/log/src/log.c)
  * [config/json/compile.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json)
  * [configure.py](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py)
  * [crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)
  * [crypto/eal/src/eal_pkey_method.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_method.c)
  * [crypto/eal/src/eal_pkey_sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_sign.c)
  * [crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
  * [crypto/ealinit/src/asmcap_alg_asm.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_alg_asm.c)
  * [crypto/ealinit/src/asmcap_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h)
  * [crypto/ealinit/src/crypt_init.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c)
  * [crypto/include/crypt_arm.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_arm.h)
  * [crypto/rsa/src/rsa_keyop.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_keyop.c)
  * [docs/en/4_User Guide/1_Build and Installation Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User Guide/1_Build and Installation Guide.md)
  * [include/bsl/bsl_log.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/bsl/bsl_log.h)
  * [testcode/demo/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt)
  * [testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
  * [testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c)
  * [testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)
  * [testcode/demo/privpass_token.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c)
  * [testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
  * [testcode/demo/sm2enc.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c)
  * [testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c)
  * [testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c)
  * [testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c)
  * [testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c)

This guide provides step-by-step instructions for obtaining, building, and
using the openHiTLS library. The page focuses on getting a working
installation of openHiTLS and running your first applications with it. For
detailed documentation on specific components, please refer to their
respective wiki pages.

## Prerequisites

Before you begin, ensure you have the following tools installed:

Tool| Recommended Version| Description  
---|---|---  
GCC| ≥ 7.3.0| C compiler  
Python| ≥ 3.5| Required for build configuration  
CMake| ≥ 3.16| Build system  
SCTP| Any version| Optional, required only for DTLS feature  
  
Sources: [docs/en/4_User Guide/1_Build and Installation
Guide.md4-14](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User
Guide/1_Build and Installation Guide.md#L4-L14)

## Obtaining the Source Code

There are two ways to obtain the openHiTLS source code:

### Method 1: Clone the Main Repository and Dependencies Separately

    
    
    # Clone the main repository
    git clone https://gitcode.com/openhitls/openhitls.git
    
    # Navigate to the project directory
    cd openhitls
    
    # Clone the required Secure C dependency
    git clone https://gitee.com/openeuler/libboundscheck platform/Secure_C

### Method 2: Clone with Submodules (Recommended)

    
    
    # Clone the repository with all submodules
    git clone --recurse-submodules https://gitcode.com/openhitls/openhitls.git

Sources:
[README.md32-39](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L32-L39)
[docs/en/4_User Guide/1_Build and Installation
Guide.md16-33](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User
Guide/1_Build and Installation Guide.md#L16-L33)

## Building the Dependencies

Before building openHiTLS, you need to build the Secure C library:

    
    
    cd platform/Secure_C
    make -j

Sources:
[README.md42-45](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L42-L45)

## Building openHiTLS

The build process involves configuring the build options, generating build
scripts with CMake, and compiling the code:

### Step 1: Create a Build Directory

    
    
    cd openHiTLS
    mkdir -p ./build
    cd ./build

### Step 2: Configure the Build

Use the `configure.py` script to select which components and features to
build. The basic syntax is:

    
    
    python3 ../configure.py [options]

Common configuration options include:

    
    
    # Build all components with static libraries
    python3 ../configure.py --enable hitls_bsl hitls_crypto hitls_tls hitls_pki hitls_auth --lib_type static --bits=64 --system=linux
    
    # Build with x86-64 assembly optimizations
    python3 ../configure.py --enable hitls_bsl hitls_crypto hitls_tls hitls_pki hitls_auth --lib_type static --bits=64 --system=linux --asm_type x8664

### Step 3: Generate Build Scripts

    
    
    cmake ..

### Step 4: Build and Install

    
    
    make
    make install

Sources:
[README.md67-96](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L67-L96)
[configure.py15-71](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L15-L71)
[.github/workflows/cmake-single-
platform.yml28-36](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L28-L36)

## Build System Architecture

The build system of openHiTLS is designed to be flexible, allowing you to
select which components and features to include in your build.

    
    
    configure.py
    
    Parse Arguments
    
    Update Configurations
    
    Generate modules.cmake
    
    CMake Build Process
    
    feature.json
    
    compile.json
    
    Feature Selections
    
    Compiler Options
    
    Assembly Optimizations
    
    Compiled Libraries
    
    Test Executables

Sources:
[configure.py15-71](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L15-L71)
[configure.py146-417](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L146-L417)

## Project Structure

The openHiTLS repository is organized into several directories, each
containing a different component:

    
    
    └── openHiTLS
       ├── bsl                # Base Support Layer - core utilities
       ├── crypto             # Cryptographic operations
       ├── tls                # TLS protocol implementation
       ├── pki                # PKI functionality
       ├── auth               # Authentication services
       ├── include            # Public header files
       ├── platform           # Platform-specific code and dependencies
       ├── testcode           # Test code and examples
       └── ...                # Build and configuration files
    

Sources: [docs/en/4_User Guide/1_Build and Installation
Guide.md37-57](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User
Guide/1_Build and Installation Guide.md#L37-L57)

## Architecture Overview

openHiTLS follows a layered architecture designed to provide a flexible,
secure, and efficient implementation of cryptographic services and TLS
protocols.

    
    
    Basic Support Layer
    
    Applications
    
    TLS Protocol Layer
    
    Cryptographic Services Layer
    
    Provider Framework
    
    Logging
    
    Memory Management
    
    OS Abstraction
    
    I/O Handling

Sources: [architecture diagram from prompt]

## Basic Usage Examples

### Initializing the Library

Before using any functionality, you need to initialize the cryptographic
services and set up memory handling:

    
    
    #include "bsl_sal.h"
    #include "bsl_err.h"
    #include "crypt_eal_init.h"
    #include "crypt_algid.h"
    #include "crypt_eal_rand.h"
    
    // Register memory management functions
    BSL_SAL_CallBack_Ctrl(BSL_SAL_MEM_MALLOC_CB_FUNC, malloc);
    BSL_SAL_CallBack_Ctrl(BSL_SAL_MEM_FREE_CB_FUNC, free);
    BSL_ERR_Init();
    
    // Initialize the cryptographic engine
    int32_t ret = CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
    if (ret != CRYPT_SUCCESS) {
        printf("CRYPT_EAL_Init: error code is %x\n", ret);
        return ret;
    }
    
    // Initialize random number generator
    ret = CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    if (ret != CRYPT_SUCCESS) {
        printf("Init rand failed.\n");
        return ret;
    }

Sources:
[testcode/demo/client.c39-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L39-L53)
[testcode/demo/server.c43-57](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L43-L57)
[testcode/demo/drbg.c44-58](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c#L44-L58)

### Creating a TLS Client

Below is a simplified flow for creating a TLS client:

    
    
    NetworkBSL_UIOHITLS_CtxHITLS_ConfigApplicationNetworkBSL_UIOHITLS_CtxHITLS_ConfigApplicationHITLS_CFG_NewTLS12Config()Configure certificate settingsHITLS_New(config)BSL_UIO_New(BSL_UIO_TcpMethod())BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, &fd)HITLS_SetUio(ctx, uio)HITLS_Connect(ctx)HITLS_Write(ctx, data, length, &written)HITLS_Read(ctx, buffer, maxLength, &read)HITLS_Close(ctx)HITLS_Free(ctx)HITLS_CFG_FreeConfig(config)

Example client code:

    
    
    // Create TLS configuration
    HITLS_Config *config = HITLS_CFG_NewTLS12Config();
    if (config == NULL) {
        printf("HITLS_CFG_NewTLS12Config failed.\n");
        return -1;
    }
    
    // Load certificates
    HITLS_X509_Cert *rootCA = NULL;
    HITLS_X509_CertParseFile(BSL_FORMAT_ASN1, "path/to/ca.der", &rootCA);
    HITLS_CFG_AddCertToStore(config, rootCA, TLS_CERT_STORE_TYPE_DEFAULT, true);
    
    // Create TLS context
    HITLS_Ctx *ctx = HITLS_New(config);
    if (ctx == NULL) {
        printf("HITLS_New failed.\n");
        return -1;
    }
    
    // Setup I/O
    BSL_UIO *uio = BSL_UIO_New(BSL_UIO_TcpMethod());
    BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, sizeof(fd), &fd);
    HITLS_SetUio(ctx, uio);
    
    // Establish connection
    ret = HITLS_Connect(ctx);
    if (ret != HITLS_SUCCESS) {
        printf("HITLS_Connect failed, ret = 0x%x.\n", ret);
        return -1;
    }
    
    // Send/receive data
    HITLS_Write(ctx, data, dataLen, &writtenLen);
    HITLS_Read(ctx, buffer, bufferLen, &readLen);
    
    // Cleanup
    HITLS_Close(ctx);
    HITLS_Free(ctx);
    HITLS_CFG_FreeConfig(config);
    HITLS_X509_CertFree(rootCA);
    BSL_UIO_Free(uio);

Sources:
[testcode/demo/client.c82-146](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L82-L146)

### Creating a TLS Server

The server setup is similar to the client, but uses `HITLS_Accept` instead of
`HITLS_Connect`:

    
    
    // Create TLS configuration
    HITLS_Config *config = HITLS_CFG_NewTLS12Config();
    
    // Configure server certificates
    HITLS_CFG_LoadCertFile(config, "path/to/server.der", TLS_PARSE_FORMAT_ASN1);
    HITLS_CFG_LoadKeyFile(config, "path/to/server.key.der", TLS_PARSE_FORMAT_ASN1);
    
    // Create TLS context
    HITLS_Ctx *ctx = HITLS_New(config);
    
    // Setup I/O with the client socket
    BSL_UIO *uio = BSL_UIO_New(BSL_UIO_TcpMethod());
    BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, sizeof(fd), &clientfd);
    HITLS_SetUio(ctx, uio);
    
    // Accept incoming connection
    ret = HITLS_Accept(ctx);
    if (ret != HITLS_SUCCESS) {
        printf("HITLS_Accept failed, ret = 0x%x.\n", ret);
        return -1;
    }
    
    // Receive/send data
    HITLS_Read(ctx, buffer, bufferLen, &readLen);
    HITLS_Write(ctx, response, responseLen, &writtenLen);
    
    // Cleanup
    HITLS_Close(ctx);
    HITLS_Free(ctx);
    HITLS_CFG_FreeConfig(config);
    BSL_UIO_Free(uio);

Sources:
[testcode/demo/server.c94-174](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L94-L174)

### Using Cryptographic Functions

openHiTLS provides a wide range of cryptographic functions. Here's an example
of using DRBG (Deterministic Random Bit Generator):

    
    
    // Initialize random number generator
    ret = CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    if (ret != CRYPT_SUCCESS) {
        printf("RandInit: error code is %x\n", ret);
        return ret;
    }
    
    // Generate random bytes
    uint8_t output[100];
    ret = CRYPT_EAL_RandbytesEx(NULL, output, sizeof(output));
    if (ret != CRYPT_SUCCESS) {
        printf("CRYPT_EAL_Randbytes: error code is %x\n", ret);
        return ret;
    }
    
    // Clean up
    CRYPT_EAL_RandDeinit();

Sources:
[testcode/demo/drbg.c60-106](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c#L60-L106)

## Cleanup and Deinitialization

Always make sure to properly release resources when you're done:

    
    
    // Release TLS resources
    HITLS_Close(ctx);
    HITLS_Free(ctx);
    HITLS_CFG_FreeConfig(config);
    
    // Release cryptographic resources
    CRYPT_EAL_RandDeinit();
    
    // Release error handling resources
    BSL_ERR_DeInit();

Sources:
[testcode/demo/client.c163-170](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L163-L170)
[testcode/demo/drbg.c105-107](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c#L105-L107)

## Next Steps

After getting familiar with the basics, you might want to explore:

  1. More advanced TLS configurations in [TLS Protocol Implementation](/openHiTLS/openHiTLS/4-tls-protocol-implementation)
  2. Cryptographic services available in [Cryptographic Services](/openHiTLS/openHiTLS/3-cryptographic-services)
  3. How to integrate with different systems using [Building and Configuration](/openHiTLS/openHiTLS/5-building-and-configuration)
  4. Advanced usage patterns in [Developer Guides](/openHiTLS/openHiTLS/6-developer-guides)

# Architecture

Relevant source files

  * [crypto/drbg/include/crypt_drbg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/include/crypt_drbg.h)
  * [crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)
  * [crypto/eal/src/eal_md.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c)
  * [crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
  * [crypto/include/crypt_local_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_local_types.h)
  * [crypto/provider/src/default/crypt_default_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c)
  * [crypto/provider/src/default/crypt_default_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c)
  * [docs/en/5_Developer Guide/4_provider Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md)
  * [docs/index/index.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/index/index.md)
  * [include/crypto/crypt_eal_implprovider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h)
  * [include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)
  * [include/crypto/crypt_eal_rand.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_rand.h)
  * [include/crypto/crypt_errno.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h)
  * [include/crypto/crypt_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_types.h)
  * [include/tls/hitls_crypt_type.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_crypt_type.h)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data)
  * [testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c)
  * [testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c)
  * [tls/config/src/config_group.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c)
  * [tls/crypt/crypt_adapt/crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_adapt/crypt.c)
  * [tls/handshake/common/include/hs_ctx.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_ctx.h)
  * [tls/handshake/common/src/hs_kx.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c)
  * [tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
  * [tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)
  * [tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)

This document provides a comprehensive overview of the openHiTLS architecture,
detailing the system's layered design, major components, and their
interactions. It serves as a reference for developers working with the
codebase, explaining how the different subsystems fit together. For specific
implementation details about cryptographic providers, refer to Provider
Development Guide.

## Layered Architecture Overview

The openHiTLS project implements a hierarchical layered architecture designed
to separate concerns, enhance modularity, and provide abstraction barriers
between functionally distinct components.

    
    
    Basic Support Layer (BSL)
    
    Provider Framework
    
    Cryptographic Services Layer (EAL)
    
    TLS Protocol Layer
    
    Application Layer
    
    Client/Server Applications
    
    Handshake Protocol
    
    Record Protocol
    
    Alert Protocol
    
    Symmetric Encryption
    
    Asymmetric Cryptography
    
    Hash Functions
    
    MAC Functions
    
    Random Number Generation
    
    Key Derivation
    
    Provider Manager
    
    Default Provider
    
    Custom Providers
    
    Logging
    
    Memory Management
    
    OS Abstraction
    
    I/O Handling
    
    ASN.1/PEM Encoding

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md1-514](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L1-L514)
  * [include/crypto/crypt_eal_implprovider.h1-283](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h#L1-L283)
  * [crypto/eal/src/eal_pkey_gen.c16-138](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L16-L138)

## Provider Framework

The Provider Framework is a critical architectural component that enables
extensibility through a plugin architecture for cryptographic implementations.

    
    
    Provider Framework
    
    CRYPT_EAL_LibCtx
    
    Provider Manager
    
    Provider Discovery & Loading
    
    Algorithm Selection
    
    Provider Scoring
    
    Dynamic Library Loading
    
    Provider Initialization
    
    Algorithm Registry
    
    Attribute Matching
    
    Mandatory Attribute Filtering
    
    Optional Attribute Scoring
    
    Default Provider
    
    Custom Providers
    
    Application
    
    Cryptographic Operations

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md22-194](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L22-L194)
  * [include/crypto/crypt_eal_implprovider.h22-106](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h#L22-L106)
  * [crypto/provider/src/default/crypt_default_provider.c38-82](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L38-L82)

### Provider Model

The provider model enables pluggable cryptographic implementations, allowing
applications to:

  1. **Use multiple implementations concurrently** : Different algorithms can be supplied by different providers
  2. **Select specific implementations** : Based on hardware acceleration, security certifications, or other criteria
  3. **Dynamically load providers** : Using the provider loading mechanism

Each provider registers itself with the framework by implementing the
`CRYPT_EAL_ProviderInit` function, which is called when the provider is
loaded:

    
    
    int32_t CRYPT_EAL_ProviderInit(CRYPT_EAL_ProvMgrCtx *mgrCtx,
                                  BSL_Param *param,
                                  CRYPT_EAL_Func *capFuncs,
                                  CRYPT_EAL_Func **outFuncs,
                                  void **provCtx);

Providers expose their algorithms through a defined interface structure that
maps operations to implementations:

    
    
    typedef struct {
        int32_t algId;                // Algorithm identifier
        const CRYPT_EAL_Func *implFunc; // Implementation functions
        const char *attr;             // Algorithm attributes
    } CRYPT_EAL_AlgInfo;

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md283-327](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L283-L327)
  * [include/crypto/crypt_eal_implprovider.h37-41](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h#L37-L41)
  * [crypto/provider/src/default/crypt_default_provider.c40-81](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L40-L81)

### Algorithm Discovery and Selection

Algorithm selection follows a sophisticated process:

  1. The framework first identifies providers that implement the requested algorithm ID
  2. If multiple providers implement the same algorithm, selection is based on: 
     * Mandatory attribute requirements (equality, non-equality)
     * Optional attribute preferences (each match increases score)
  3. The highest-scoring provider is selected for the operation

The attribute mechanism consists of name-value pairs (format: `name=value`),
which enable fine-grained algorithm selection.

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md242-274](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L242-L274)
  * [crypto/provider/src/default/crypt_default_provider.c410-434](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L410-L434)

## Cryptographic Services Layer

The Cryptographic Services Layer (EAL - Ecosystem Abstraction Layer) provides
a uniform interface to cryptographic primitives, abstracting away the details
of specific implementations.

    
    
    Cryptographic Services Layer
    
    EAL Interface
    
    Symmetric Encryption
    
    Asymmetric Cryptography
    
    Hash Functions
    
    MAC Functions
    
    Random Number Generation
    
    Key Derivation
    
    AES (128/192/256)
    
    ChaCha20
    
    SM4
    
    RSA
    
    DSA
    
    ECDSA
    
    ECDH
    
    SM2
    
    Ed25519/X25519
    
    Post-Quantum Algorithms
    
    Hybrid KEM
    
    SHA-1/2/3
    
    SM3
    
    MD5
    
    HMAC
    
    CMAC
    
    GMAC
    
    DRBG
    
    HKDF
    
    PBKDF2
    
    SCRYPT

Sources:

  * [include/crypto/crypt_types.h34-546](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_types.h#L34-L546)
  * [crypto/eal/src/eal_pkey_gen.c35-753](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L35-L753)
  * [crypto/include/crypt_local_types.h32-198](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_local_types.h#L32-L198)

### Public Key Operations

Public key operations are implemented through the `CRYPT_EAL_PkeyCtx`
structure which encapsulates all asymmetric cryptography functionality:

  1. **Key Generation** : Creating new key pairs
  2. **Digital Signatures** : Signing and verifying data
  3. **Key Exchange** : Establishing shared secrets
  4. **Encryption/Decryption** : Asymmetric encryption
  5. **Key Encapsulation** : Support for KEM algorithms

The EAL layer provides unified API functions such as `CRYPT_EAL_PkeyNewCtx()`,
`CRYPT_EAL_PkeySetPrv()`, `CRYPT_EAL_PkeySign()`, etc., that map to their
provider-specific implementations.

Sources:

  * [crypto/eal/src/eal_pkey_gen.c70-167](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L70-L167)
  * [include/crypto/crypt_eal_pkey.h40-81](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L40-L81)

### Hash Functions

The message digest module is implemented through the `CRYPT_EAL_MdCTX`
structure that provides:

  1. **Context Management** : Creation, duplication, and destruction of hash contexts
  2. **Incremental Hashing** : Initialization, updates, and finalization
  3. **Single-shot Operations** : Hashing complete data with a single function call

The module supports a wide range of hash algorithms including SHA-1/2/3, SM3,
and MD5.

Sources:

  * [crypto/eal/src/eal_md.c36-73](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c#L36-L73)
  * [crypto/include/crypt_local_types.h32-71](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_local_types.h#L32-L71)

### Random Number Generation

The DRBG (Deterministic Random Bit Generator) system provides secure random
number generation for the library:

    
    
    CRYPT_EAL_RandInit
    
    DRBG Initialization
    
    Entropy Collection
    
    DRBG Instantiation
    
    Entropy Sources
    
    Hardware Sources
    
    OS-provided Sources
    
    DRBG Algorithms
    
    Hash-based DRBG
    
    HMAC-based DRBG
    
    CTR-based DRBG
    
    CRYPT_EAL_RandBytes
    
    DRBG Generation
    
    Internal State Update
    
    Reseeding

The DRBG module includes:

  1. **Entropy Sourcing** : Collecting unpredictable data from the environment
  2. **State Management** : Maintaining and protecting the internal DRBG state
  3. **Periodic Reseeding** : Ensuring continued randomness
  4. **Algorithm Support** : Multiple DRBG mechanisms (Hash, HMAC, CTR)

Sources:

  * [crypto/drbg/src/drbg.c34-598](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L34-L598)
  * [include/crypto/crypt_eal_rand.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_rand.h)
  * [crypto/provider/src/default/crypt_default_rand.c29-52](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c#L29-L52)

## TLS Protocol Layer

The TLS Protocol Layer implements the secure communication protocols,
supporting TLS 1.2, TLS 1.3, and DTLS.

    
    
    TLS Protocol Layer
    
    TLS_Ctx
    
    Handshake Module
    
    Record Module
    
    Alert Module
    
    Session Management
    
    Key Exchange
    
    ECDHE
    
    DHE
    
    RSA
    
    PSK
    
    KEM
    
    Certificate Handling
    
    Extensions Processing
    
    Record Encryption/Decryption
    
    Record Fragmentation
    
    Alert Generation
    
    Alert Processing

Sources:

  * [tls/handshake/common/src/hs_kx.c38-202](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L38-L202)
  * [tls/handshake/pack/src/pack_extensions.c46-180](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L46-L180)
  * [tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)

### Key Exchange

The key exchange subsystem supports multiple algorithms for establishing
shared secrets:

  1. **ECDHE** : Elliptic Curve Diffie-Hellman Ephemeral
  2. **DHE** : Diffie-Hellman Ephemeral
  3. **RSA** : For legacy key exchange
  4. **PSK** : Pre-Shared Keys
  5. **KEM** : Key Encapsulation Mechanisms (for post-quantum)

The `KeyExchCtx` structure encapsulates all key exchange state and operations:

    
    
    KeyExchCtx *HS_KeyExchCtxNew(void);
    void HS_KeyExchCtxFree(KeyExchCtx *keyExchCtx);
    int32_t HS_ProcessServerKxMsgEcdhe(TLS_Ctx *ctx, const ServerKeyExchangeMsg *serverKxMsg);
    int32_t HS_ProcessClientKxMsgEcdhe(TLS_Ctx *ctx, const ClientKeyExchangeMsg *clientKxMsg);

Sources:

  * [tls/handshake/common/src/hs_kx.c38-99](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L38-L99)
  * [tls/handshake/common/src/hs_kx.c100-237](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L100-L237)
  * [tls/handshake/common/include/hs_ctx.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_ctx.h)

### Extensions Handling

TLS extensions enable negotiation of protocol features and parameters. The
extension subsystem handles:

  1. **Extension Serialization** : Formatting extensions for transmission
  2. **Extension Parsing** : Extracting extensions from received messages
  3. **Extension Processing** : Applying the semantics of each extension

Key extension types include:

  * Server Name Indication (SNI)
  * Supported Groups (elliptic curves, finite fields)
  * Signature Algorithms
  * Key Share (TLS 1.3)
  * Pre-Shared Key (TLS 1.3)
  * Cookie (TLS 1.3)

Sources:

  * [tls/handshake/pack/src/pack_extensions.c51-179](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L51-L179)
  * [tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)

## Integration and Configuration

The openHiTLS system includes a flexible configuration mechanism for
customizing behavior at different levels:

  1. **Build Configuration** : Compile-time feature selection
  2. **Runtime Configuration** : Setting protocol parameters and security options
  3. **Provider Configuration** : Selecting and configuring cryptographic providers

Key configuration areas include:

  * Supported protocol versions
  * Cipher suite preferences
  * Cryptographic provider selection
  * Session management policies
  * Certificate validation options

Sources:

  * [tls/config/src/config_group.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c)
  * [testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c)

## Error Handling Model

The error handling system provides detailed error information across all
layers:

  1. **Error Codes** : Hierarchical numbering system for error identification
  2. **Error Propagation** : Consistent passing of errors up the call stack
  3. **Error Reporting** : Detailed error information for debugging

The `CRYPT_ERRORs` enumerated in `crypt_errno.h` define the possible error
conditions:

    
    
    enum CRYPT_ERROR {
        CRYPT_NULL_INPUT = 0x01010001,      // Null pointer input error
        CRYPT_SECUREC_FAIL,                 // Security function error
        CRYPT_MEM_ALLOC_FAIL,               // Memory allocation failure
        // ... other error codes
    };

Sources:

  * [include/crypto/crypt_errno.h40-419](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h#L40-L419)
  * [bsl_err_internal.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl_err_internal.h) (referenced in multiple files)

## Summary

The openHiTLS architecture combines a layered design with a provider-based
extension model to create a flexible, secure, and efficient TLS
implementation. The clear separation of concerns between the TLS protocol
layer, cryptographic services layer, and provider framework enables:

  1. **Extensibility** : New cryptographic algorithms can be added without modifying the core
  2. **Platform Independence** : The BSL layer abstracts OS-specific functionality
  3. **Performance Optimization** : Specialized implementations can be selected based on hardware capabilities
  4. **Security Isolation** : Clear boundaries between components limit the impact of vulnerabilities

This design supports the project's goal of providing a modern, secure TLS
implementation suitable for a wide range of applications.

# Provider Framework

Relevant source files

  * [config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)
  * [crypto/drbg/include/crypt_drbg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/include/crypt_drbg.h)
  * [crypto/eal/src/eal_md.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c)
  * [crypto/hybridkem/include/crypt_hybridkem.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/include/crypt_hybridkem.h)
  * [crypto/include/crypt_local_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_local_types.h)
  * [crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)
  * [crypto/provider/src/mgr/crypt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c)
  * [docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md)
  * [docs/en/5_Developer Guide/4_provider Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md)
  * [docs/index/index.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/index/index.md)
  * [include/crypto/crypt_eal_implprovider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h)
  * [include/crypto/crypt_eal_init.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h)
  * [include/crypto/crypt_eal_rand.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_rand.h)
  * [include/crypto/crypt_errno.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h)
  * [include/crypto/crypt_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_types.h)
  * [testcode/script/execute_sdv.sh](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/script/execute_sdv.sh)
  * [testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c)
  * [testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c)

The Provider Framework is a core component of openHiTLS that enables flexible
and dynamic loading of cryptographic implementations. It creates a layer of
abstraction between the Cryptographic Services Layer and the actual
implementations of cryptographic algorithms, allowing different providers to
offer various implementations of the same algorithm optimized for different
environments or security requirements.

For information about the overall architecture of openHiTLS, see
[Architecture](/openHiTLS/openHiTLS/2-architecture).

## Architecture

The Provider Framework acts as a mediator between the Cryptographic Services
Layer and the actual implementations of cryptographic algorithms. It manages
multiple providers, each offering various algorithm implementations.

    
    
    Provider Framework
    
    Provider Manager
    
    Provider Loading/Unloading
    
    Algorithm Discovery
    
    Provider Selection
    
    Default Provider
    
    Dynamic Loading
    
    Algorithm Capabilities Query
    
    Scoring/Prioritization
    
    Default Implementations
    
    Custom Implementations
    
    Hardware-optimized Implementations
    
    Generic Implementations

The Provider Framework consists of several key components:

  * **Library Context** : Central structure managing the lifecycle of loaded providers
  * **Provider Manager** : Handles provider loading, unloading, and selection
  * **Algorithm Discovery** : Mechanism for querying available algorithms from providers
  * **Provider Selection** : Logic for choosing the best provider based on capabilities and attributes

Sources:
[include/crypto/crypt_eal_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_provider.h)
[crypto/provider/src/mgr/crypt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c)
[docs/en/5_Developer Guide/4_provider Development
Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md)

## Core Components

### Library Context

The Library Context (`CRYPT_EAL_LibCtx`) is the primary structure that manages
the list of loaded providers, configurations, and resources.

Library contexts can be managed with these functions:

  * `CRYPT_EAL_LibCtxNew()`: Creates a new library context
  * `CRYPT_EAL_LibCtxFree()`: Releases all resources associated with a library context

Sources:
[crypto/provider/include/crypt_provider.h35-40](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h#L35-L40)

### Provider Manager Context

The Provider Manager Context (`CRYPT_EAL_ProvMgrCtx`) represents a loaded
provider and maintains:

  * Provider name and path
  * Dynamic library handle
  * Reference count
  * Provider's algorithm implementations
  * Provider-specific data

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md12-13](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L12-L13)

## Provider Lifecycle

### Loading and Unloading

The framework supports loading providers dynamically at runtime:

Key functions for provider management:

  * `CRYPT_EAL_ProviderSetLoadPath()`: Sets the search path for providers
  * `CRYPT_EAL_ProviderLoad()`: Loads a provider from a dynamic library or built-in implementation
  * `CRYPT_EAL_ProviderUnload()`: Unloads a provider and frees associated resources

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md57-93](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L57-L93)
[crypto/provider/src/mgr/crypt_provider.c104-142](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c#L104-L142)

## Algorithm Discovery and Provider Selection

### Algorithm Query

Applications can query for algorithms provided by loaded providers:

    
    
    int32_t CRYPT_EAL_ProviderGetFuncs(
        CRYPT_EAL_LibCtx *libCtx,     // Library context
        int32_t operaId,              // Algorithm category ID
        int32_t algId,                // Algorithm ID
        const char *attribute,        // Attribute string for filtering
        const CRYPT_EAL_Func **funcs, // Output: algorithm functions
        void **provCtx                // Output: provider context
    );

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md116-132](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L116-L132)

### Attribute Mechanism and Provider Scoring

The Provider Framework uses an attribute-based scoring system to select the
most appropriate provider for a given operation:

  * Attributes are key-value pairs describing algorithm characteristics (e.g., `name=md5,type=hash,version=1.0`)
  * Queries can include mandatory conditions (`=`, `!=`) and optional conditions (`?`)
  * Providers matching optional conditions receive higher scores
  * The provider with the highest score is selected

Example attribute query:

    
    
    name=md5,feature?attr_good,feature?attr_good,feature?attr_bad
    

In this example:

  * `name=md5` is a mandatory condition
  * `feature?attr_good` is an optional condition (appears twice, adding +2 to score)
  * `feature?attr_bad` is another optional condition (+1 to score)

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md244-279](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L244-L279)

## Using Provider-Based Algorithms

The EAL (Ecosystem Abstraction Layer) provides wrapper interfaces that
simplify using provider-based algorithms:

Example using provider-based MD5 hashing:

    
    
    // Create MD5 context from a provider
    CRYPT_EAL_MdCTX *ctx = CRYPT_EAL_ProviderMdNewCtx(libCtx, CRYPT_MD_MD5, "provider=default");
    
    // Use standard API with provider-based implementation
    CRYPT_EAL_MdInit(ctx);
    CRYPT_EAL_MdUpdate(ctx, data, dataLen);
    CRYPT_EAL_MdFinal(ctx, output, &outLen);
    CRYPT_EAL_MdFreeCtx(ctx);

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md99-109](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L99-L109)
[crypto/eal/src/eal_md.c151-189](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c#L151-L189)

## Developing Custom Providers

To create a custom provider, developers must implement:

  1. Provider initialization function:
         
         int32_t CRYPT_EAL_ProviderInit(
             CRYPT_EAL_ProvMgrCtx *mgrCtx,  // Provider manager context
             BSL_Param *param,              // Additional parameters
             CRYPT_EAL_Func *capFuncs,      // Framework's capability functions
             CRYPT_EAL_Func **outFuncs,     // Provider's exposed functions
             void **provCtx                 // Provider-specific context
         );

  2. Algorithm query function:
         
         int32_t CRYPT_EAL_ProvQueryCb(
             void *provCtx,               // Provider context
             int32_t operaId,             // Algorithm category ID
             CRYPT_EAL_AlgInfo **algInfos // Provider's algorithm information
         );

  3. Algorithm implementations for supported operations (symmetric cipher, hash, MAC, etc.)

  4. Optional capabilities reporting:
         
         int32_t CRYPT_EAL_ProvGetCapsCb(
             void *provCtx,              // Provider context
             int32_t cmd,                // Command (e.g., CRYPT_EAL_GET_GROUP_CAP)
             CRYPT_EAL_ProcCapsCb cb,    // Callback for reporting capabilities
             void *args                  // Additional arguments
         );

Sources:
[include/crypto/crypt_eal_implprovider.h104-105](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h#L104-L105)
[docs/en/5_Developer Guide/4_provider Development
Guide.md289-307](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L289-L307)

## Error Handling

The Provider Framework uses error codes defined in `crypt_errno.h`. Common
provider-related error codes include:

Error Code| Description  
---|---  
`CRYPT_PROVIDER_ERR_UNEXPECTED_IMPL`| Unexpected implementation  
`CRYPT_PROVIDER_ERR_IMPL_NULL`| Implementation function is NULL  
`CRYPT_PROVIDER_NOT_FOUND`| Provider not found  
`CRYPT_PROVIDER_ERR_NEWCTX`| Failed to create context  
`CRYPT_PROVIDER_NOT_SUPPORT`| Provider does not support the requested
operation  
`CRYPT_PROVIDER_ERR_ATTRIBUTE`| Invalid attribute  
`CRYPT_PROVIDER_INVALID_LIB_CTX`| Invalid library context  
  
Sources:
[include/crypto/crypt_errno.h477-483](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h#L477-L483)

## Example: Provider Framework Usage

    
    
    // Create a library context
    CRYPT_EAL_LibCtx *libCtx = CRYPT_EAL_LibCtxNew();
    assert(libCtx != NULL);
    
    // Set the provider loading path
    int ret = CRYPT_EAL_ProviderSetLoadPath(libCtx, "/path/to/providers");
    assert(ret == CRYPT_SUCCESS);
    
    // Load a provider
    ret = CRYPT_EAL_ProviderLoad(libCtx, BSL_SAL_CONVERTER_SO, "provider_name", NULL, NULL);
    assert(ret == CRYPT_SUCCESS);
    
    // Use a provider-based algorithm with attribute matching
    CRYPT_EAL_MdCTX *ctx = CRYPT_EAL_ProviderMdNewCtx(libCtx, CRYPT_MD_MD5, "name=md5,type=hash");
    assert(ctx != NULL);
    
    // Use the algorithm with standard API functions
    ret = CRYPT_EAL_MdInit(ctx);
    ret = CRYPT_EAL_MdUpdate(ctx, data, dataLen);
    ret = CRYPT_EAL_MdFinal(ctx, output, &outLen);
    
    // Clean up resources
    CRYPT_EAL_MdFreeCtx(ctx);
    ret = CRYPT_EAL_ProviderUnload(libCtx, BSL_SAL_CONVERTER_SO, "provider_name");
    CRYPT_EAL_LibCtxFree(libCtx);

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md440-511](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L440-L511)
[testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c130-168](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c#L130-L168)

## Integration with the Global Context

Applications can also use the Provider Framework with the global library
context:

    
    
    // Set path and load provider in global context
    CRYPT_EAL_ProviderSetLoadPath(NULL, "/path/to/providers");
    CRYPT_EAL_ProviderLoad(NULL, BSL_SAL_CONVERTER_SO, "provider_name", NULL, NULL);
    
    // Use a provider-based algorithm with global context
    CRYPT_EAL_MdCTX *ctx = CRYPT_EAL_ProviderMdNewCtx(NULL, CRYPT_MD_MD5, "provider=default");
    
    // Use the algorithm
    CRYPT_EAL_MdInit(ctx);
    CRYPT_EAL_MdUpdate(ctx, data, dataLen);
    CRYPT_EAL_MdFinal(ctx, output, &outLen);
    
    // Clean up
    CRYPT_EAL_MdFreeCtx(ctx);
    CRYPT_EAL_ProviderUnload(NULL, BSL_SAL_CONVERTER_SO, "provider_name");

The global context is initialized during library startup and can be cleaned up
with `CRYPT_EAL_Cleanup()` when no longer needed.

Sources:
[testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c234-254](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c#L234-L254)
[include/crypto/crypt_eal_init.h52-60](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h#L52-L60)

# Error Handling

Relevant source files

  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)
  * [crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
  * [crypto/include/crypt_local_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_local_types.h)
  * [crypto/provider/src/default/crypt_default_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c)
  * [crypto/rsa/src/rsa_encdec.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c)
  * [include/crypto/crypt_eal_implprovider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h)
  * [include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)
  * [include/crypto/crypt_errno.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h)
  * [include/crypto/crypt_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_types.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data)
  * [testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)

## Purpose and Scope

This document describes the error handling system within the openHiTLS
library. The system provides a consistent approach for detecting, reporting,
propagating, and recovering from errors throughout the codebase. Understanding
this system is essential for both library users and developers who need to
properly interpret errors and implement error handling in new components.

For information about specific TLS protocol errors, see [TLS Protocol
Implementation](/openHiTLS/openHiTLS/4-tls-protocol-implementation).

## Error Code Architecture

The error handling system in openHiTLS is built around a structured error code
system that categorizes errors by module and type. This hierarchical approach
allows for precise identification of error sources.

    
    
    Error Code Structure 0xMMSSEEEE
    
    Module ID (MM)
    
    Submodule ID (SS)
    
    Error Code (EEEE)
    
    01: Crypto
    
    02: TLS
    
    Other modules
    
    01: Generic errors
    
    02: Big Number operations
    
    03: RSA operations
    
    04: EAL errors
    
    05+: Other submodules
    
    0001: First error in category
    
    0002: Second error in category
    
    ...and so on

Sources:
[include/crypto/crypt_errno.h40-513](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h#L40-L513)
[include/tls/hitls_error.h81-187](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L81-L187)

### Success Codes

Successful operations are uniformly represented across modules:

    
    
    CRYPT_SUCCESS = 0     // Success code for crypto operations
    HITLS_SUCCESS = 0     // Success code for TLS operations
    

### TLS-Specific Status Codes

The TLS module includes special status codes (1-6) that indicate non-error
states requiring specific handling:

Status Code| Symbolic Name| Meaning  
---|---|---  
1| HITLS_WANT_CONNECT| Connection blocked, call HITLS_Connect again  
2| HITLS_WANT_ACCEPT| Connection blocked, call HITLS_Accept again  
3| HITLS_WANT_READ| Receiving buffer is empty, retry operation  
4| HITLS_WANT_WRITE| Sending buffer is full, retry operation  
5| HITLS_ERR_TLS| Unrecoverable protocol error  
6| HITLS_ERR_SYSCALL| Unrecoverable I/O error  
  
Sources:
[include/tls/hitls_error.h41-74](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L41-L74)

### Common Error Categories

The error code system covers several error categories:

  1. **Input Validation Errors** : Null pointers, invalid arguments (e.g., `CRYPT_NULL_INPUT`, `HITLS_INVALID_INPUT`)
  2. **Resource Errors** : Memory allocation failures (e.g., `CRYPT_MEM_ALLOC_FAIL`, `HITLS_MEMALLOC_FAIL`)
  3. **Buffer Errors** : Insufficient buffer space (e.g., `CRYPT_RSA_BUFF_LEN_NOT_ENOUGH`)
  4. **Algorithm-Specific Errors** : Issues with cryptographic operations (e.g., `CRYPT_BN_ERR_DIVISOR_ZERO`)
  5. **Protocol Errors** : TLS protocol issues (e.g., `HITLS_MSG_HANDLE_UNEXPECTED_MESSAGE`)
  6. **State Errors** : Incorrect operational state (e.g., `CRYPT_DRBG_ERR_STATE`)

Sources:
[include/crypto/crypt_errno.h40-513](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h#L40-L513)
[include/tls/hitls_error.h81-187](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L81-L187)

## Error Reporting Mechanisms

openHiTLS employs a multi-layered approach to error reporting, combining error
code returns with internal error tracking and event reporting.

### Error Reporting Flow

    
    
    "EAL Error System""BSL Error System""Library Function""Application""EAL Error System""BSL Error System""Library Function""Application"Function callDetect errorBSL_ERR_PUSH_ERROR(error_code)Add error to stackEAL_ERR_REPORT(event, algo, id, error)Log error eventreturn error_codeHandle or propagate error

Sources:
[crypto/eal/src/eal_pkey_gen.c74-76](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L74-L76)
[crypto/eal/src/eal_pkey_gen.c148-150](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L148-L150)
[crypto/drbg/src/drbg.c94-97](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L94-L97)

### BSL Error Stack

The Basic Support Layer (BSL) maintains an error stack that allows error
information to be pushed and retrieved. Key functions include:

  * `BSL_ERR_PUSH_ERROR`: Records an error code in the error stack
  * `BSL_ERR_GET_ERROR`: Retrieves the last error from the stack
  * `BSL_ERR_CLEAR_ERROR`: Clears the error stack

Example usage:

    
    
    if (pkey == NULL) {
        BSL_ERR_PUSH_ERROR(CRYPT_NULL_INPUT);
        return CRYPT_NULL_INPUT;
    }

Sources:
[crypto/eal/src/eal_pkey_gen.c149](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L149-L149)
[crypto/rsa/src/rsa_encdec.c49](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L49-L49)

### EAL Error Reporting

The Ecosystem Abstraction Layer (EAL) provides more detailed error reporting
with contextual information:

  * `EAL_ERR_REPORT`: Records an error with algorithm and context details
  * `EAL_EventReport`: Records successful operations or specific events

Example usage:

    
    
    if (method == NULL) {
        EAL_ERR_REPORT(CRYPT_EVENT_ERR, CRYPT_ALGO_PKEY, id, CRYPT_EAL_ERR_ALGID);
        return NULL;
    }

Sources:
[crypto/eal/src/eal_pkey_gen.c75](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L75-L75)
[crypto/eal/src/eal_pkey_gen.c502](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L502-L502)

## Error Handling Patterns

The codebase employs consistent patterns for error handling to ensure proper
detection, reporting, and cleanup.

### Standard Error Handling Flow

    
    
    Valid
    
    Invalid
    
    Success
    
    Failure
    
    Success
    
    Failure
    
    Function Entry
    
    Input Validation
    
    Resource Allocation
    
    Report Error
    
    Return Error Code
    
    Main Operation
    
    Report Resource Error
    
    Cleanup
    
    Success Reporting
    
    Report Operation Error
    
    Cleanup
    
    Return Success

Sources:
[crypto/rsa/src/rsa_encdec.c454-502](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L454-L502)
[crypto/drbg/src/drbg.c271-332](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L271-L332)

### Input Validation Pattern

All functions begin with input validation to ensure parameters are valid:

    
    
    if (ctx == NULL || input == NULL || out == NULL || outLen == NULL) {
        BSL_ERR_PUSH_ERROR(CRYPT_NULL_INPUT);
        return CRYPT_NULL_INPUT;
    }

Sources:
[crypto/rsa/src/rsa_encdec.c463-466](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L463-L466)
[crypto/eal/src/eal_pkey_gen.c148-151](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L148-L151)

### Error Cleanup with GOTO

For functions with complex resource allocation, a goto pattern ensures proper
cleanup when errors occur:

    
    
    BN_BigNum *result = BN_Create(bits + 1);
    if (result == NULL) {
        BSL_ERR_PUSH_ERROR(CRYPT_MEM_ALLOC_FAIL);
        return CRYPT_MEM_ALLOC_FAIL;
    }
    
    // Additional operations that might fail
    int32_t ret = SomeOperation();
    if (ret != CRYPT_SUCCESS) {
        goto ERR;
    }
    
    return CRYPT_SUCCESS;
    
    ERR:
    BN_Destroy(result);
    return ret;

Sources:
[crypto/rsa/src/rsa_encdec.c110-115](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L110-L115)
[crypto/rsa/src/rsa_encdec.c175-177](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L175-L177)

### Error Propagation

When a called function returns an error, it's typically propagated upward with
additional context:

    
    
    ret = DRBG_GetEntropy(ctx, &entropy, addEntropy);
    if (ret != CRYPT_SUCCESS) {
        BSL_ERR_PUSH_ERROR(ret);
        goto ERR;
    }

Sources:
[crypto/drbg/src/drbg.c308-312](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L308-L312)
[crypto/rsa/src/rsa_encdec.c490](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L490-L490)

## State Management and Error Recovery

Several components in openHiTLS use explicit state management to track
operational status and facilitate error recovery.

### DRBG State Management

The Deterministic Random Bit Generator (DRBG) implements a state machine to
manage its operational status:

When errors occur, the DRBG transitions to an error state and provides
mechanisms to recover by uninstantiating and reinstantiating the generator.

Sources:
[crypto/drbg/src/drbg.c300](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L300-L300)
[crypto/drbg/src/drbg.c380](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L380-L380)

### Resource Cleanup

The codebase consistently implements resource cleanup routines to prevent
resource leaks when errors occur:

    
    
    static void RsaDecProcedureFree(RsaDecProcedurePara *para)
    {
        if (para == NULL) {
            return;
        }
        BN_Destroy(para->cP);
        BN_Destroy(para->cQ);
        BN_Destroy(para->mP);
        BN_Destroy(para->mQ);
        BN_MontDestroy(para->montP);
        BN_MontDestroy(para->montQ);
    }

Sources:
[crypto/rsa/src/rsa_encdec.c184-195](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L184-L195)
[crypto/eal/src/eal_pkey_gen.c185-206](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L185-L206)

### Automatic Reseed for DRBG

The DRBG component implements automatic error recovery by reseeding when
necessary:

    
    
    if (DRBG_IsNeedReseed(ctx, pr)) {
        ret = DRBG_Reseed(ctx, adin, adinLen, NULL);
        if (ret != CRYPT_SUCCESS) {
            BSL_ERR_PUSH_ERROR(ret);
            return ret;
        }
        // Reset after successful reseed
        adinData.data = NULL;
        adinData.len = 0;
    }

Sources:
[crypto/drbg/src/drbg.c428-436](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L428-L436)

## Best Practices for Error Handling

When implementing new code or working with openHiTLS, follow these guidelines
for consistent error handling:

  1. **Always check return values** from functions that can fail
  2. **Push errors to the BSL error stack** using `BSL_ERR_PUSH_ERROR`
  3. **Report detailed error events** using `EAL_ERR_REPORT` where appropriate
  4. **Clean up all resources** when errors occur
  5. **Use goto patterns** for complex functions with multiple cleanup needs
  6. **Maintain consistent state** by explicitly tracking and managing operational state
  7. **Provide recovery mechanisms** for recoverable error conditions

Sources:
[crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
[crypto/rsa/src/rsa_encdec.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c)
[crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)

# Cryptographic Services

Relevant source files

  * [crypto/curve25519/src/curve25519.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/curve25519/src/curve25519.c)
  * [crypto/dh/src/dh_core.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/dh/src/dh_core.c)
  * [crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)
  * [crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
  * [crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
  * [crypto/ecc/src/ecc_pkey.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecc_pkey.c)
  * [crypto/ecc/src/ecp_mont.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecp_mont.c)
  * [crypto/hpke/src/hpke.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c)
  * [crypto/hybridkem/src/crypt_hybridkem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c)
  * [crypto/hybridkem/src/crypt_hybridkem_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem_local.h)
  * [crypto/mldsa/src/ml_dsa.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/mldsa/src/ml_dsa.c)
  * [crypto/provider/src/default/crypt_default_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c)
  * [include/crypto/crypt_eal_hpke.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_hpke.h)
  * [include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)
  * [include/crypto/crypt_params_key.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_params_key.h)
  * [testcode/demo/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt)
  * [testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
  * [testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c)
  * [testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)
  * [testcode/demo/privpass_token.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c)
  * [testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
  * [testcode/demo/sm2enc.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c)
  * [testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c)
  * [testcode/framework/include/helper.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/include/helper.h)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data)
  * [testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.c)
  * [testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.data)
  * [testcode/testdata/provider/provider_get_cap_test1.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/testdata/provider/provider_get_cap_test1.c)
  * [tls/crypt/crypt_self/hitls_crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_self/hitls_crypt.c)

The Cryptographic Services layer provides a comprehensive suite of
cryptographic primitives and functions for the openHiTLS library. It serves as
the foundation for secure communications and encryption operations, sitting
between the TLS Protocol Layer and the Provider Framework in the overall
architecture. This component is responsible for implementing various
cryptographic algorithms, managing keys, and providing secure random number
generation.

## Architecture Overview

The Cryptographic Services layer is structured around the Ecosystem
Abstraction Layer (EAL) interface, which provides uniform access to various
cryptographic primitives regardless of their underlying implementation.

    
    
    Cryptographic Services Layer
    
    Ecosystem Abstraction Layer (EAL)
    
    CRYPT_EAL_PkeyCtx (Public Key)
    
    CRYPT_EAL_RndCtx (Random Number Generation)
    
    CRYPT_EAL_HpkeCtx (Hybrid PKE)
    
    CRYPT_EAL_CipherCtx (Symmetric Encryption)
    
    CRYPT_EAL_MdCtx (Hash Functions)
    
    CRYPT_EAL_MacCtx (MAC Functions)
    
    CRYPT_EAL_KdfCTX (Key Derivation)
    
    RSA
    
    ECDSA/ECDH
    
    SM2
    
    Ed25519/X25519
    
    Hybrid KEM
    
    DRBG_Ctx
    
    Hash DRBG
    
    HMAC DRBG
    
    CTR DRBG
    
    KEM (Key Encapsulation)
    
    KDF (Key Derivation)
    
    AEAD (Authenticated Encryption)
    
    AES (CBC, GCM, CTR)
    
    ChaCha20-Poly1305
    
    SM4
    
    SHA-1/2/3
    
    SM3
    
    MD5
    
    HMAC
    
    CMAC
    
    GMAC
    
    HKDF
    
    PBKDF2
    
    SCRYPT

Sources:
[crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
[crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
[crypto/hpke/src/hpke.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c)
[crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)

## Provider Framework Integration

The Cryptographic Services layer uses a Provider Framework that allows for
pluggable implementations of cryptographic algorithms. This enables hardware
acceleration when available and allows users to integrate custom
implementations.

    
    
    Application
    
    Cryptographic Services Layer
    
    EAL Interface
    
    Provider Framework
    
    CRYPT_EAL_Provider
    
    Default Provider
    
    Hardware Provider
    
    Custom Provider
    
    Software Implementations
    
    Hardware-accelerated Implementations
    
    User-defined Implementations

Sources:
[crypto/provider/src/default/crypt_default_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c)
[crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)

## Key Components

### Public Key Operations (CRYPT_EAL_PkeyCtx)

The public key operations module provides a unified interface for asymmetric
cryptography operations including key generation, signing, verification,
encryption, decryption, and key exchange.

    
    
    CRYPT_EAL_PkeyCtx
    
    Key Generation (CRYPT_EAL_PkeyGen)
    
    Parameter Management
    
    CRYPT_EAL_PkeySetPara
    
    CRYPT_EAL_PkeyGetPara
    
    Key Management
    
    CRYPT_EAL_PkeySetPub
    
    CRYPT_EAL_PkeySetPrv
    
    CRYPT_EAL_PkeyGetPub
    
    CRYPT_EAL_PkeyGetPrv
    
    Cryptographic Operations
    
    CRYPT_EAL_PkeySign
    
    CRYPT_EAL_PkeyVerify
    
    CRYPT_EAL_PkeyEncrypt
    
    CRYPT_EAL_PkeyDecrypt
    
    CRYPT_EAL_PkeyComputeShareKey

The `CRYPT_EAL_PkeyCtx` structure manages public key operations for various
algorithms including RSA, ECDSA, SM2, Ed25519, and X25519. Key structures for
public and private keys are defined in separate structures.

Sources:
[crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
[include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)

### Random Number Generation (CRYPT_EAL_RndCtx)

The random number generation module provides secure random bytes for
cryptographic operations using Deterministic Random Bit Generators (DRBG).

    
    
    CRYPT_EAL_RndCtx
    
    Initialization
    
    CRYPT_EAL_RandInit
    
    CRYPT_EAL_DrbgInstantiate
    
    Random Byte Generation
    
    CRYPT_EAL_Randbytes
    
    CRYPT_EAL_RandbytesWithAdin
    
    Seeding
    
    CRYPT_EAL_RandSeed
    
    CRYPT_EAL_RandSeedWithAdin
    
    Deinitialization
    
    CRYPT_EAL_RandDeinit

The `CRYPT_EAL_RndCtx` structure manages random number generation through a
DRBG (Deterministic Random Bit Generator) implementation. The system supports
multiple DRBG algorithms including Hash-based, HMAC-based, and CTR-based
DRBGs.

Sources:
[crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
[crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)

### Hybrid Public Key Encryption (CRYPT_EAL_HpkeCtx)

The HPKE module provides hybrid public key encryption according to RFC 9180.
It combines key encapsulation mechanisms, key derivation functions, and
authenticated encryption.

    
    
    CRYPT_EAL_HpkeCtx
    
    Context Creation
    
    CRYPT_EAL_HpkeNewCtx
    
    Sender Operations
    
    CRYPT_EAL_HpkeSeal
    
    CRYPT_EAL_HpkeEncrypt
    
    CRYPT_EAL_HpkeExport
    
    Recipient Operations
    
    CRYPT_EAL_HpkeOpen
    
    CRYPT_EAL_HpkeDecrypt
    
    CRYPT_EAL_HpkeExport
    
    Parameters
    
    CRYPT_HPKE_Role (SENDER/RECIPIENT)
    
    CRYPT_HPKE_Mode (BASE/PSK/AUTH/AUTH_PSK)
    
    CRYPT_HPKE_CipherSuite (KEM/KDF/AEAD)

The `CRYPT_EAL_HpkeCtx` structure manages the state for Hybrid Public Key
Encryption operations, supporting different modes (Base, PSK, Auth, AuthPSK)
and roles (Sender, Recipient).

Sources:
[crypto/hpke/src/hpke.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c)
[include/crypto/crypt_eal_hpke.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_hpke.h)

### Hybrid Key Encapsulation Mechanism (CRYPT_HybridKemCtx)

The Hybrid KEM module provides key encapsulation mechanisms that combine
traditional (elliptic curve based) and post-quantum approaches for forward
security.

    
    
    CRYPT_HybridKemCtx
    
    Context Creation
    
    CRYPT_HYBRID_KEM_NewCtx
    
    Key Management
    
    CRYPT_HYBRID_KEM_SetKeyType
    
    CRYPT_HYBRID_KEM_GenerateKey
    
    Encapsulation/Decapsulation
    
    CRYPT_HYBRID_KEM_Encaps
    
    CRYPT_HYBRID_KEM_Decaps
    
    Hybrid Algorithms
    
    CRYPT_HYBRID_X25519_MLKEM512
    
    CRYPT_HYBRID_X25519_MLKEM768
    
    CRYPT_HYBRID_X25519_MLKEM1024
    
    CRYPT_HYBRID_ECDH_NISTP256_MLKEM512
    
    CRYPT_HYBRID_ECDH_NISTP384_MLKEM768
    
    CRYPT_HYBRID_ECDH_NISTP521_MLKEM1024

Sources:
[crypto/hybridkem/src/crypt_hybridkem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c)
[crypto/hybridkem/src/crypt_hybridkem_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem_local.h)

## Supported Algorithms

The Cryptographic Services Layer supports a wide range of cryptographic
algorithms:

Category| Algorithms  
---|---  
Symmetric Encryption| AES (128, 192, 256 bits) in CBC, GCM, CTR modes  
ChaCha20-Poly1305  
SM4 (Chinese standard)  
Asymmetric Cryptography| RSA (signatures and encryption)  
ECDSA (with NIST P-256, P-384, P-521 curves)  
SM2 (Chinese standard)  
Ed25519 (signatures)  
X25519 (key exchange)  
Hybrid KEM  
Post-quantum algorithms (ML-KEM, SLH-DSA)  
Hash Functions| SHA-1, SHA-2 (224, 256, 384, 512), SHA-3  
SM3 (Chinese standard)  
MD5 (legacy support)  
MAC Functions| HMAC (with various hash functions)  
CMAC (Cipher-based MAC)  
GMAC (Galois MAC)  
Key Derivation| HKDF (HMAC-based Key Derivation Function)  
PBKDF2 (Password-Based Key Derivation Function 2)  
SCRYPT (memory-hard key derivation function)  
  
## Parameter Handling

The Cryptographic Services Layer uses a flexible parameter system defined in
[include/crypto/crypt_params_key.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_params_key.h)
for passing various options and configurations to cryptographic operations:

    
    
    // Parameter IDs for public key operations
    #define CRYPT_PARAM_EC_POINT_UNCOMPRESSED     (CRYPT_PARAM_EC_BASE + 1)
    #define CRYPT_PARAM_EC_PRVKEY                 (CRYPT_PARAM_EC_BASE + 2)
    #define CRYPT_PARAM_EC_P                      (CRYPT_PARAM_EC_BASE + 3)
    
    // Parameter IDs for key derivation functions
    #define CRYPT_PARAM_KDF_PASSWORD     (CRYPT_PARAM_KDF_BASE + 1)
    #define CRYPT_PARAM_KDF_MAC_ID       (CRYPT_PARAM_KDF_BASE + 2)
    #define CRYPT_PARAM_KDF_SALT         (CRYPT_PARAM_KDF_BASE + 3)
    
    // Parameter IDs for random number generation
    #define CRYPT_PARAM_RAND_SEEDCTX          (CRYPT_PARAM_RAND_BASE + 1)
    #define CRYPT_PARAM_RAND_PR               (CRYPT_PARAM_RAND_BASE + 2)
    #define CRYPT_PARAM_RAND_SEED_GETENTROPY  (CRYPT_PARAM_RAND_BASE + 3)
    

Parameters are passed using the `BSL_Param` structure, which allows for type-
safe parameter passing.

Sources:
[include/crypto/crypt_params_key.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_params_key.h)

## Usage Examples

### Random Number Generation

Example from
[testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c):

    
    
    // Initialize the DRBG
    ret = CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
    ret = CRYPT_EAL_RandInit(CRYPT_RAND_SHA256, NULL, NULL, NULL, 0);
    
    // Generate random bytes
    uint8_t randomData[32];
    ret = CRYPT_EAL_Randbytes(randomData, sizeof(randomData));
    
    // Clean up
    CRYPT_EAL_RandDeinit();

### Key Generation and Signing

Example from
[testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c):

    
    
    // Create a new SM2 key context
    CRYPT_EAL_PkeyCtx *pkey = CRYPT_EAL_PkeyNewCtx(CRYPT_PKEY_SM2);
    
    // Generate key pair
    ret = CRYPT_EAL_PkeyGen(pkey);
    
    // Sign data
    uint8_t signature[64];
    uint32_t signatureLen = sizeof(signature);
    ret = CRYPT_EAL_PkeySign(pkey, data, dataLen, signature, &signatureLen);
    
    // Verify signature
    ret = CRYPT_EAL_PkeyVerify(pkey, data, dataLen, signature, signatureLen);
    
    // Clean up
    CRYPT_EAL_PkeyFreeCtx(pkey);

### TLS Client/Server Communication

Examples from
[testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
and
[testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
show how the Cryptographic Services Layer is used in TLS communication:

    
    
    // Initialize cryptographic services
    ret = CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
    ret = CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Create TLS configuration
    config = HITLS_CFG_NewTLS12Config();
    
    // Set up certificate and private key
    HITLS_CFG_LoadCertFile(config, "server.der", TLS_PARSE_FORMAT_ASN1);
    HITLS_CFG_LoadKeyFile(config, "server.key.der", TLS_PARSE_FORMAT_ASN1);
    
    // Create TLS context and perform handshake
    ctx = HITLS_New(config);
    ret = HITLS_Accept(ctx);  // Server side
    ret = HITLS_Connect(ctx); // Client side
    
    // Exchange data
    ret = HITLS_Write(ctx, data, dataLen, &writtenLen);
    ret = HITLS_Read(ctx, buffer, bufferLen, &readLen);
    
    // Clean up
    HITLS_Close(ctx);
    HITLS_Free(ctx);

## Integration with TLS

The Cryptographic Services Layer is tightly integrated with the TLS Protocol
Layer, providing the necessary cryptographic primitives for secure
communication. The TLS Protocol Layer uses the Cryptographic Services Layer
for:

  1. Random number generation during the TLS handshake
  2. Key exchange using asymmetric cryptography
  3. Certificate verification using public key operations
  4. Symmetric encryption of application data
  5. Message authentication using MAC functions
  6. Key derivation for session keys

This integration enables the TLS Protocol Layer to implement various TLS
versions (1.2, 1.3) and cipher suites, providing secure communication for
applications.

Sources:
[testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
[testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
[tls/crypt/crypt_self/hitls_crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_self/hitls_crypt.c)

## Summary

The Cryptographic Services Layer provides a comprehensive suite of
cryptographic primitives for the openHiTLS project. It supports a wide range
of algorithms for symmetric and asymmetric encryption, hash functions, MAC
functions, random number generation, and key derivation. The layer is designed
with a Provider Framework that allows for pluggable implementations, enabling
hardware acceleration and custom implementations. Through its well-defined
interfaces, it serves as the security foundation for the entire openHiTLS
library.

# Random Number Generation

Relevant source files

  * [.github/workflows/cmake-single-platform.yml](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-single-platform.yml)
  * [config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)
  * [crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)
  * [crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)
  * [crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
  * [crypto/eal/src/eal_pkey_method.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_method.c)
  * [crypto/eal/src/eal_pkey_sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_sign.c)
  * [crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
  * [crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)
  * [crypto/provider/src/default/crypt_default_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c)
  * [crypto/rsa/src/rsa_keyop.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_keyop.c)
  * [docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md)
  * [include/crypto/crypt_eal_init.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h)
  * [include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)
  * [testcode/demo/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt)
  * [testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
  * [testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c)
  * [testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)
  * [testcode/demo/privpass_token.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c)
  * [testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
  * [testcode/demo/sm2enc.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c)
  * [testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data)
  * [testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c)

This document describes the random number generation system in openHiTLS,
which provides cryptographically secure random numbers essential for TLS
operations. It details the architecture of the Deterministic Random Bit
Generator (DRBG) implementation, supported entropy sources, and usage
patterns.

## Overview

The random number generation system in openHiTLS follows NIST SP 800-90A
standards, implementing several types of Deterministic Random Bit Generators
(DRBGs). This system is critical for security-sensitive operations such as key
generation, nonce creation, and other cryptographic procedures where
unpredictability is essential.

### Key Features

  * Multiple DRBG algorithm implementations (Hash-based, HMAC-based, and CTR-based)
  * Configurable entropy sources
  * Automatic and manual reseeding capabilities
  * Support for both global and context-specific random number generators
  * Provider framework for algorithm implementations

Sources:
[crypto/eal/src/eal_rand.c594-625](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L594-L625)
[crypto/drbg/src/drbg.c557-598](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L557-L598)

## Architecture

The random number generation system in openHiTLS is structured in a layered
architecture with several key components.

    
    
    Entropy Sources
    
    DRBG Types
    
    Applications
    
    CRYPT_EAL_Randbytes API
    
    Context-specific API
    
    Global DRBG Context
    
    Context-specific DRBG
    
    DRBG Implementation
    
    Entropy Sources
    
    Hash-based DRBG
    
    HMAC-based DRBG
    
    CTR-based DRBG
    
    /dev/random
    
    getentropy()
    
    System entropy
    
    Hardware entropy

Sources:
[crypto/eal/src/eal_rand.c50-56](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L50-L56)
[crypto/eal/src/eal_rand.c522-528](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L522-L528)
[crypto/drbg/src/drbg.c186-255](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L186-L255)

### Core Components

  1. **DRBG Context (`CRYPT_EAL_RndCtx`)**: Contains the state and methods for a specific DRBG instance
  2. **Global DRBG (`g_globalRndCtx`)**: A singleton DRBG instance used by the global API functions
  3. **Seed DRBG (`g_seedDrbg`)**: A special DRBG used as an entropy source for other DRBGs when enabled
  4. **Provider Framework** : Allows plugging in different implementations of DRBG algorithms

Sources:
[crypto/eal/src/eal_rand.c523](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L523-L523)
[crypto/eal/src/eal_rand.c52-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L52-L53)

### DRBG Types

The system supports three main types of DRBGs:

DRBG Type| Description| Algorithms| Feature Flag  
---|---|---|---  
Hash-based| Uses cryptographic hash functions| SHA1, SHA224, SHA256, SHA384,
SHA512, SM3| HITLS_CRYPTO_DRBG_HASH  
HMAC-based| Uses HMAC with hash functions| HMAC-SHA1, HMAC-SHA224, HMAC-
SHA256, HMAC-SHA384, HMAC-SHA512| HITLS_CRYPTO_DRBG_HMAC  
CTR-based| Uses block ciphers in counter mode| AES-128, AES-192, AES-256, SM4|
HITLS_CRYPTO_DRBG_CTR  
  
Sources:
[crypto/drbg/src/drbg.c559-586](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L559-L586)
[config/macro_config/hitls_config_layer_crypto.h122-132](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L122-L132)

### Entropy Sources

Entropy is crucial for the security of random number generation. The system
supports various entropy sources:

  1. **`/dev/random`** : Uses the system's random device (enabled with HITLS_CRYPTO_ENTROPY_DEVRANDOM)
  2. **`getentropy()`** : Uses the getentropy system call (enabled with HITLS_CRYPTO_ENTROPY_GETENTROPY)
  3. **System entropy** : Uses system-specific entropy sources (enabled with HITLS_CRYPTO_ENTROPY_SYS)
  4. **Hardware entropy** : Uses hardware entropy sources (enabled with HITLS_CRYPTO_ENTROPY_HARDWARE)

If no specific entropy source is configured, `/dev/random` is used by default.

Sources:
[config/macro_config/hitls_config_layer_crypto.h112-119](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L112-L119)
[crypto/eal/src/eal_rand.c387-402](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L387-L402)

## DRBG Lifecycle

The lifecycle of a DRBG in openHiTLS follows a standard pattern:

    
    
    Instantiate
    
    Seed with entropy
    
    Reseed
    
    Error condition
    
    Recover
    
    Uninstantiate
    
    Free
    
    Uninitialized
    
    Initialized
    
    Ready
    
    Error

Sources:
[crypto/drbg/src/drbg.c257-496](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L257-L496)

### Initialization

DRBGs are initialized with seed material, which includes entropy input and
optional personalization data. The instantiation process consists of:

  1. Collecting entropy from configured sources
  2. Optionally collecting a nonce
  3. Processing the seed material according to the specific DRBG algorithm
  4. Setting the initial state of the DRBG

Sources:
[crypto/drbg/src/drbg.c271-333](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L271-L333)

### Random Bit Generation

Once initialized, a DRBG can generate random bits. The generation process:

  1. Checks if reseeding is needed (based on invocation count or time)
  2. Updates the internal state
  3. Produces the requested number of random bits
  4. Updates the state again

Sources:
[crypto/drbg/src/drbg.c408-447](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L408-L447)

### Reseeding

DRBGs must be reseeded periodically to maintain their security. Reseeding can
occur:

  1. Automatically after a configurable number of invocations (default: 10000)
  2. Automatically after a configurable time period (when GM mode is enabled)
  3. Manually via the reseed functions

The reseeding process collects fresh entropy and updates the DRBG state.

Sources:
[crypto/drbg/src/drbg.c353-406](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L353-L406)
[crypto/drbg/src/drbg.c498-556](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L498-L556)

## API Reference

The random number generation system provides two sets of APIs:

### Global DRBG API

These functions operate on a global DRBG instance shared across the
application:

Function| Description  
---|---  
`CRYPT_EAL_RandInit`| Initialize the global DRBG with specified algorithm and
parameters  
`CRYPT_EAL_ProviderRandInitCtx`| Initialize the global DRBG using the provider
framework  
`CRYPT_EAL_Randbytes`| Generate random bytes using the global DRBG  
`CRYPT_EAL_RandbytesEx`| Generate random bytes with extended parameters  
`CRYPT_EAL_RandSeed`| Reseed the global DRBG  
`CRYPT_EAL_RandSeedEx`| Reseed with extended parameters  
`CRYPT_EAL_RandDeinit`| Clean up the global DRBG  
  
Sources:
[crypto/eal/src/eal_rand.c549-625](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L549-L625)
[crypto/eal/src/eal_rand.c882-908](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L882-L908)

### Context-specific DRBG API

These functions allow creating and managing specific DRBG contexts:

Function| Description  
---|---  
`CRYPT_EAL_DrbgNew`| Create a new DRBG context  
`CRYPT_EAL_DrbgInstantiate`| Initialize a DRBG context  
`CRYPT_EAL_Drbgbytes`| Generate random bytes using a specific DRBG context  
`CRYPT_EAL_DrbgbytesWithAdin`| Generate random bytes with additional input  
`CRYPT_EAL_DrbgSeed`| Reseed a specific DRBG context  
`CRYPT_EAL_DrbgCtrl`| Configure a DRBG context  
`CRYPT_EAL_DrbgDeinit`| Clean up a DRBG context  
  
Sources:
[crypto/eal/src/eal_rand.c633-686](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L633-L686)
[crypto/eal/src/eal_rand.c670-671](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L670-L671)

## Usage Guidelines

### Basic Usage

The simplest way to use the random number generation system is through the
global DRBG:

  1. Initialize the system with `CRYPT_EAL_Init`
  2. Initialize the random number generator with `CRYPT_EAL_ProviderRandInitCtx`
  3. Generate random bytes with `CRYPT_EAL_Randbytes`
  4. Clean up with `CRYPT_EAL_RandDeinit`

Example:

    
    
    // Initialize EAL
    CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
    
    // Initialize random number generator with SHA256-based DRBG
    CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Generate random bytes
    uint8_t buffer[32];
    CRYPT_EAL_Randbytes(buffer, sizeof(buffer));
    
    // Clean up
    CRYPT_EAL_RandDeinit();

Sources:
[testcode/demo/drbg.c39-108](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c#L39-L108)

### Advanced Usage

For applications requiring multiple independent random number generators,
context-specific DRBGs can be used:

  1. Create a DRBG context with `CRYPT_EAL_DrbgNew`
  2. Initialize the DRBG with `CRYPT_EAL_DrbgInstantiate`
  3. Generate random bytes with `CRYPT_EAL_Drbgbytes`
  4. Clean up with `CRYPT_EAL_DrbgDeinit`

Sources:
[crypto/eal/src/eal_rand.c633-668](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L633-L668)

### Provider Framework Integration

For custom implementations or hardware acceleration, the provider framework
can be used:

  1. Implement the required provider interfaces
  2. Register the provider with the framework
  3. Initialize the DRBG with the custom provider

Sources:
[crypto/eal/src/eal_rand.c689-787](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L689-L787)
[crypto/provider/src/default/crypt_default_rand.c29-47](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c#L29-L47)

## Security Considerations

When using the random number generation system, consider the following
security guidelines:

  1. **Entropy Quality** : The security of the random number generation depends on the quality of the entropy sources. Ensure appropriate entropy sources are available.

  2. **Reseeding Frequency** : Regular reseeding is important for maintaining security. The default reseeding intervals are conservative, but may be adjusted based on specific threat models.

  3. **Multiple DRBGs** : If different security domains exist in your application, consider using separate DRBG contexts to maintain isolation.

  4. **Memory Management** : Ensure proper cleanup of DRBG contexts to prevent exposure of sensitive state information.

  5. **GM Compliance** : When GM (Chinese national standard) compliance is required, use the GM-specific modes and settings available in the system.

Sources:
[crypto/drbg/src/drbg.c498-523](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L498-L523)
[crypto/eal/src/eal_rand.c51-56](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L51-L56)

## Implementation Notes

The random number generation system in openHiTLS is designed to be:

  1. **Standards-compliant** : Follows NIST SP 800-90A recommendations for DRBGs
  2. **Flexible** : Supports multiple algorithms and entropy sources
  3. **Efficient** : Includes optimized implementations where available
  4. **Secure** : Incorporates best practices for cryptographic random number generation

The implementation includes automatic handling of many security requirements,
such as prediction resistance and entropy collection, making it suitable for
use in security-critical applications while minimizing the risk of misuse.

Sources:
[crypto/drbg/src/drbg.c428-447](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L428-L447)
[crypto/eal/src/eal_rand.c386-424](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L386-L424)

# Public Key Cryptography

Relevant source files

  * [crypto/curve25519/src/curve25519.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/curve25519/src/curve25519.c)
  * [crypto/dh/src/dh_core.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/dh/src/dh_core.c)
  * [crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)
  * [crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
  * [crypto/ecc/src/ecc_pkey.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecc_pkey.c)
  * [crypto/ecc/src/ecp_mont.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecp_mont.c)
  * [crypto/hpke/src/hpke.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c)
  * [crypto/hybridkem/src/crypt_hybridkem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c)
  * [crypto/hybridkem/src/crypt_hybridkem_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem_local.h)
  * [crypto/mldsa/src/ml_dsa.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/mldsa/src/ml_dsa.c)
  * [crypto/provider/src/default/crypt_default_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c)
  * [crypto/rsa/src/rsa_encdec.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c)
  * [include/crypto/crypt_eal_hpke.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_hpke.h)
  * [include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)
  * [include/crypto/crypt_params_key.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_params_key.h)
  * [testcode/framework/include/helper.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/include/helper.h)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data)
  * [testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.c)
  * [testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/hpke/test_suite_sdv_eal_hpke.data)
  * [testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c)
  * [testcode/testdata/provider/provider_get_cap_test1.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/testdata/provider/provider_get_cap_test1.c)
  * [tls/crypt/crypt_self/hitls_crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_self/hitls_crypt.c)

This page documents the public key cryptography subsystem in openHiTLS,
including supported algorithms, key operations, and integration points. It
covers the core APIs and implementation details for public key operations
including key generation, encryption/decryption, digital signatures, and key
exchange mechanisms.

For information about random number generation used by public key algorithms,
see [Random Number Generation](/openHiTLS/openHiTLS/3.1-random-number-
generation). For symmetric encryption used in hybrid schemes, see [Symmetric
Encryption](/openHiTLS/openHiTLS/3.3-symmetric-encryption). For certificate
handling and key management, see [Key and Certificate
Handling](/openHiTLS/openHiTLS/3.4-key-and-certificate-handling).

## Overview

The public key cryptography subsystem in openHiTLS provides a unified
interface for various asymmetric cryptographic algorithms through the
Ecosystem Abstraction Layer (EAL). The system supports a wide range of
traditional and post-quantum algorithms with a common API structure.

### Supported Algorithms

Algorithm Type| Variants| Operations  
---|---|---  
RSA| RSA (various bit lengths)| Encryption, Decryption, Signing, Verification  
ECC| ECDSA, ECDH, SM2| Signing, Verification, Key Exchange  
DSA| DSA| Signing, Verification  
DH| DH| Key Exchange  
Curve25519| Ed25519, X25519| Signing, Verification, Key Exchange  
Post-Quantum| ML-KEM (formerly Kyber)| Key Encapsulation  
Hybrid| Hybrid KEM (classical + post-quantum)| Key Encapsulation  
HPKE| DHKEM with various KDF/AEAD combinations| Sealed sender encryption  
  
Sources:
[include/crypto/crypt_eal_pkey.h40-81](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L40-L81)
[crypto/eal/src/eal_pkey_gen.c70-68](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L70-L68)

## Architecture

### Public Key Framework

The public key subsystem is designed around an extensible provider-based
architecture with common interfaces for different cryptographic algorithms.

    
    
    Algorithm Layer
    
    Provider Framework
    
    Public Key Interface
    
    Application Layer
    
    Application Code
    
    CRYPT_EAL_PkeyCtx
    
    CRYPT_EAL_PkeyPub/Prv
    
    Operation Functions
    
    EAL_PkeyMethod
    
    Algorithm Implementations
    
    RSA
    
    ECC/ECDSA
    
    DSA
    
    DH
    
    Ed25519/X25519
    
    Post-Quantum
    
    Hybrid KEM

Sources:
[crypto/eal/src/eal_pkey_gen.c41-68](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L41-L68)
[include/crypto/crypt_eal_pkey.h106-107](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L106-L107)

### Key Context Structure

The `CRYPT_EAL_PkeyCtx` is the central structure that manages public key
operations. It holds algorithm-specific method pointers and key data.

    
    
    contains
    
    manages
    
    manages
    
    1
    
    1
    
    CRYPT_EAL_PkeyCtx
    
    +void* key
    
    +EAL_PkeyUnitaryMethod* method
    
    +CRYPT_PKEY_AlgId id
    
    +BSL_SAL_RefCount references
    
    EAL_PkeyUnitaryMethod
    
    +newCtx()
    
    +dupCtx()
    
    +freeCtx()
    
    +setPara()
    
    +getPara()
    
    +gen()
    
    +sign()
    
    +verify()
    
    +encrypt()
    
    +decrypt()
    
    +computeShareKey()
    
    +encaps()
    
    +decaps()
    
    +blind()
    
    +unBlind()
    
    CRYPT_EAL_PkeyPub
    
    +CRYPT_PKEY_AlgId id
    
    +union key
    
    CRYPT_EAL_PkeyPrv
    
    +CRYPT_PKEY_AlgId id
    
    +union key

Sources:
[crypto/eal/src/eal_pkey_gen.c41-68](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L41-L68)
[include/crypto/crypt_eal_pkey.h40-81](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L40-L81)

## Key Operations

The public key subsystem provides a unified API for common operations across
different asymmetric algorithms:

### Key Generation

Key generation is handled by the `CRYPT_EAL_PkeyGen` function, which creates a
new key pair according to the algorithm-specific requirements.

    
    
    method->genCRYPT_EAL_PkeyCtxCRYPT_EAL_PkeyGenApplicationmethod->genCRYPT_EAL_PkeyCtxCRYPT_EAL_PkeyGenApplicationCall with contextCheck context validityCall algorithm-specific generationReturn success/failureReturn status code

Sources:
[crypto/eal/src/eal_pkey_gen.c483-504](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L483-L504)

### Digital Signatures

The signing and verification process is provided through a common interface
regardless of algorithm:

    
    
    Algorithm MethodsCRYPT_EAL_PkeyCtxCRYPT_EAL_PkeyVerifyCRYPT_EAL_PkeySignApplicationAlgorithm MethodsCRYPT_EAL_PkeyCtxCRYPT_EAL_PkeyVerifyCRYPT_EAL_PkeySignApplicationSign message with private keyValidate context and messageCall algorithm-specific signingReturn signatureReturn signatureVerify signature with public keyValidate context, message, signatureCall algorithm-specific verificationReturn verification resultReturn verification status

Sources:
[crypto/rsa/src/rsa_encdec.c505-618](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L505-L618)

### Key Exchange and Encapsulation

For key exchange (e.g., DH, ECDH) and key encapsulation mechanisms (KEMs):

    
    
    CRYPT_EAL_PkeyComputeShareKeyResponderInitiatorCRYPT_EAL_PkeyComputeShareKeyResponderInitiatorGenerate key pairSend public keyGenerate key pairCompute shared secretReturn shared secretSend public keyCompute shared secretReturn shared secret

Sources:
[crypto/hpke/src/hpke.c619-746](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c#L619-L746)

## Key Data Structures

### Public Key Structures

The `CRYPT_EAL_PkeyPub` structure contains a union of all supported algorithm-
specific public key formats:

    
    
    typedef struct {
        CRYPT_PKEY_AlgId id;  // Algorithm identifier
        union {
            CRYPT_RsaPub rsaPub;           // RSA public key
            CRYPT_DsaPub dsaPub;           // DSA public key
            CRYPT_DhPub dhPub;             // DH public key
            CRYPT_EccPub eccPub;           // ECC public key
            CRYPT_Curve25519Pub curve25519Pub; // Ed25519/X25519 public key
            CRYPT_PaillierPub paillierPub;  // Paillier public key
            CRYPT_KemEncapsKey kemEk;       // KEM encapsulation key
            CRYPT_ElGamalPub elgamalPub;    // ElGamal public key
            CRYPT_MlDsaPub mldsaPub;        // MLDSA public key
            CRYPT_SlhDsaPub slhDsaPub;      // SLH-DSA public key
        } key;
    } CRYPT_EAL_PkeyPub;
    

Sources:
[include/crypto/crypt_eal_pkey.h40-54](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L40-L54)

### Private Key Structures

Similarly, the `CRYPT_EAL_PkeyPrv` structure contains a union of all supported
algorithm-specific private key formats:

    
    
    typedef struct {
        CRYPT_PKEY_AlgId id;  // Algorithm identifier
        union {
            CRYPT_RsaPrv rsaPrv;           // RSA private key
            CRYPT_DsaPrv dsaPrv;           // DSA private key
            CRYPT_DhPrv dhPrv;             // DH private key
            CRYPT_EccPrv eccPrv;           // ECC private key
            CRYPT_Curve25519Prv curve25519Prv; // Ed25519/X25519 private key
            CRYPT_PaillierPrv paillierPrv;  // Paillier private key
            CRYPT_KemDecapsKey kemDk;       // KEM decapsulation key
            CRYPT_ElGamalPrv elgamalPrv;    // ElGamal private key
            CRYPT_MlDsaPrv mldsaPrv;        // MLDSA private key
            CRYPT_SlhDsaPrv slhDsaPrv;      // SLH-DSA private key
        } key;
    } CRYPT_EAL_PkeyPrv;
    

Sources:
[include/crypto/crypt_eal_pkey.h67-81](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L67-L81)

## Algorithm-Specific Features

### RSA

RSA supports multiple key sizes and offers various performance optimizations:

  * Chinese Remainder Theorem (CRT) for faster private key operations
  * Blinding protections against timing side-channel attacks
  * PKCS#1 v1.5 and PSS padding schemes for signatures
  * PKCS#1 v1.5 and OAEP padding schemes for encryption

Sources:
[crypto/rsa/src/rsa_encdec.c216-267](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L216-L267)

### Elliptic Curve Cryptography

ECC implementations support:

  * NIST P-curves (P-256, P-384, P-521)
  * SM2 (Chinese standard)
  * ECDSA for signatures
  * ECDH for key agreement

Sources:
[crypto/ecc/src/ecc_pkey.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecc_pkey.c)
[crypto/ecc/src/ecp_mont.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecp_mont.c)

### Curve25519

The library provides:

  * X25519 for key exchange
  * Ed25519 for signatures
  * Constant-time implementations to resist side-channel attacks

Sources:
[crypto/curve25519/src/curve25519.c31-108](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/curve25519/src/curve25519.c#L31-L108)

### Post-Quantum and Hybrid Cryptography

openHiTLS integrates post-quantum cryptography:

  * ML-KEM (formerly Kyber) key encapsulation mechanism
  * Hybrid KEM combining traditional and post-quantum algorithms
  * HPKE (Hybrid Public Key Encryption) implementations

    
    
    Hybrid KEM Architecture
    
    CRYPT_HybridKemCtx
    
    Key Generation
    
    Encapsulation
    
    Decapsulation
    
    Classical Component (e.g., X25519)
    
    Post-Quantum Component (e.g., ML-KEM)
    
    Combined Shared Secret

Sources:
[crypto/hybridkem/src/crypt_hybridkem.c19-95](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c#L19-L95)
[crypto/hybridkem/src/crypt_hybridkem_local.h22-29](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem_local.h#L22-L29)

## HPKE (Hybrid Public Key Encryption)

HPKE provides a higher-level encryption API that combines asymmetric and
symmetric cryptography for authenticated encryption scenarios:

    
    
    RecipientSenderRecipientSenderKey Encapsulation PhaseEncryption PhaseDecryption PhaseGenerate ephemeral key pairCompute shared secret using recipient's public keyDerive encryption key using KDFEncrypt message with AEAD using derived keySend encapsulated key and ciphertextCompute shared secret using private keyDerive decryption key using KDFDecrypt ciphertext using AEAD

HPKE supports multiple modes:

  * Base mode (unauthenticated)
  * PSK mode (with pre-shared key)
  * Auth mode (with sender authentication)
  * AuthPSK mode (with both PSK and sender authentication)

Sources:
[crypto/hpke/src/hpke.c236-285](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c#L236-L285)
[crypto/hpke/src/hpke.c286-332](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hpke/src/hpke.c#L286-L332)

## API Usage

### Context Creation and Management

    
    
    // Create a new key context
    CRYPT_EAL_PkeyCtx *pkey = CRYPT_EAL_PkeyNewCtx(CRYPT_PKEY_RSA);
    
    // Free a key context
    CRYPT_EAL_PkeyFreeCtx(pkey);
    
    // Duplicate a key context
    CRYPT_EAL_PkeyCtx *newPkey = CRYPT_EAL_PkeyDupCtx(pkey);

Sources:
[crypto/eal/src/eal_pkey_gen.c106-206](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L106-L206)

### Key Generation

    
    
    // Generate a new key pair
    int32_t ret = CRYPT_EAL_PkeyGen(pkey);

Sources:
[crypto/eal/src/eal_pkey_gen.c483-504](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L483-L504)

### Key Import/Export

    
    
    // Set/import a public key
    CRYPT_EAL_PkeyPub pubKey = {/* ... */};
    int32_t ret = CRYPT_EAL_PkeySetPub(pkey, &pubKey);
    
    // Set/import a private key
    CRYPT_EAL_PkeyPrv prvKey = {/* ... */};
    int32_t ret = CRYPT_EAL_PkeySetPrv(pkey, &prvKey);
    
    // Get/export a public key
    CRYPT_EAL_PkeyPub pubKey = {/* ... */};
    int32_t ret = CRYPT_EAL_PkeyGetPub(pkey, &pubKey);

Sources:
[crypto/eal/src/eal_pkey_gen.c532-953](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L532-L953)

### Parameter Control

    
    
    // Set algorithm-specific parameters
    int32_t ret = CRYPT_EAL_PkeyCtrl(pkey, CRYPT_CTRL_SET_PARA_BY_ID, &paramId, sizeof(paramId));

Sources:
[crypto/eal/src/eal_pkey_gen.c460-476](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L460-L476)

## Random Number Generation Integration

Public key operations rely on secure random number generation for key
generation, padding, blinding, and other randomized operations. The system
interfaces with the cryptographic random number generation subsystem
documented in [Random Number Generation](/openHiTLS/openHiTLS/3.1-random-
number-generation).

    
    
    Public Key Operations
    
    CRYPT_EAL_PkeyGen
    
    RSA Blinding
    
    Padding Generation
    
    Random Number Generation Subsystem
    
    DRBG Implementation

Sources:
[crypto/drbg/src/drbg.c270-447](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L270-L447)

## Security Features

The public key implementation includes several security features:

  1. **Side-Channel Protection** :

     * Constant-time implementations for critical operations
     * Blinding for RSA private key operations
     * Secure memory handling for sensitive data
  2. **Post-Quantum Readiness** :

     * Support for ML-KEM algorithms
     * Hybrid mechanisms to combine classical and post-quantum security
  3. **Formal Standards Compliance** :

     * Implementations following NIST, IETF, and other standards
     * Support for RFC9180 (HPKE)

Sources:
[crypto/rsa/src/rsa_encdec.c270-385](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c#L270-L385)
[crypto/hybridkem/src/crypt_hybridkem.c277-349](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c#L277-L349)

## Provider Integration

The public key subsystem integrates with the Provider Framework (see [Provider
Framework](/openHiTLS/openHiTLS/2.1-provider-framework)) to allow custom
implementations of cryptographic algorithms. This enables hardware
acceleration, FIPS-compliant implementations, or alternative algorithm
implementations.

    
    
    Application
    
    CRYPT_EAL_PkeyNewCtx
    
    Default Provider
    
    Hardware Provider
    
    FIPS Provider

Sources:
[include/crypto/crypt_eal_pkey.h142-145](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L142-L145)
[crypto/provider/src/default/crypt_default_rand.c18-75](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c#L18-L75)

# Symmetric Encryption

Relevant source files

  * [.github/workflows/cmake-single-platform.yml](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-single-platform.yml)
  * [config/json/complete_options.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/complete_options.json)
  * [config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)
  * [crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)
  * [crypto/eal/src/eal_pkey_method.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_method.c)
  * [crypto/eal/src/eal_pkey_sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_sign.c)
  * [crypto/hybridkem/include/crypt_hybridkem.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/include/crypt_hybridkem.h)
  * [crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)
  * [crypto/provider/src/mgr/crypt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c)
  * [crypto/rsa/src/rsa_keyop.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_keyop.c)
  * [crypto/sha1/src/noasm_sha1.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1.c)
  * [crypto/sha1/src/noasm_sha1_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1_small.c)
  * [crypto/sha2/src/noasm_sha256.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256.c)
  * [crypto/sha2/src/noasm_sha256_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256_small.c)
  * [crypto/sha2/src/noasm_sha512.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512.c)
  * [crypto/sha2/src/noasm_sha512_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512_small.c)
  * [crypto/sm3/src/noasm_sm3.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sm3/src/noasm_sm3.c)
  * [docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md)
  * [include/crypto/crypt_eal_init.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h)
  * [testcode/script/execute_sdv.sh](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/script/execute_sdv.sh)
  * [testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c)
  * [testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c)
  * [testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c)

This page documents the symmetric encryption capabilities of the openHiTLS
cryptographic library. Symmetric encryption is a critical component of the
cryptographic services layer that enables secure data protection through
efficient encryption and decryption using the same key. For asymmetric
encryption capabilities, see [Public Key
Cryptography](/openHiTLS/openHiTLS/3.2-public-key-cryptography).

## Overview

The openHiTLS library provides a comprehensive set of symmetric encryption
algorithms and modes of operation that can be used for various security
applications. The symmetric encryption subsystem is designed to be flexible,
efficient, and secure, with support for hardware acceleration on compatible
platforms.

### Supported Algorithms and Modes

    
    
    Symmetric Encryption in openHiTLS
    
    CRYPT_CIPHER
    
    Algorithms
    
    Modes
    
    AES
    
    SM4
    
    ChaCha20
    
    CBC - Cipher Block Chaining
    
    CTR - Counter
    
    ECB - Electronic Codebook
    
    GCM - Galois/Counter Mode
    
    CCM - Counter with CBC-MAC
    
    XTS - XEX-based tweaked-codebook mode with ciphertext stealing
    
    CFB - Cipher Feedback
    
    OFB - Output Feedback
    
    ChaCha20Poly1305

Sources:
[config/macro_config/hitls_config_layer_crypto.h215-235](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L215-L235)
[config/macro_config/hitls_config_layer_crypto.h237-266](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L237-L266)

The library supports the following symmetric encryption algorithms:

Algorithm| Key Sizes| Description  
---|---|---  
AES| 128, 192, 256 bits| Advanced Encryption Standard, widely used block
cipher  
SM4| 128 bits| Chinese national standard block cipher (GB/T 32907-2016)  
ChaCha20| 256 bits| High-speed stream cipher designed by Daniel J. Bernstein  
  
The library supports the following modes of operation:

Mode| Type| Authentication| Description  
---|---|---|---  
CBC| Block| No| Cipher Block Chaining mode  
CTR| Stream| No| Counter mode - converts block cipher to stream cipher  
ECB| Block| No| Electronic Codebook mode (least secure, not recommended for
most applications)  
GCM| AEAD| Yes| Galois/Counter Mode - provides both encryption and
authentication  
CCM| AEAD| Yes| Counter with CBC-MAC - provides both encryption and
authentication  
XTS| Block| No| XEX-based tweaked-codebook mode with ciphertext stealing (used
for disk encryption)  
CFB| Stream| No| Cipher Feedback mode  
OFB| Stream| No| Output Feedback mode  
ChaCha20Poly1305| AEAD| Yes| ChaCha20 stream cipher with Poly1305 MAC for
authentication  
  
## Architecture

The symmetric encryption capabilities are integrated into the overall
openHiTLS architecture as follows:

    
    
    Cryptographic Services
    
    Applications
    
    TLS Protocol Layer
    
    Cryptographic Services Layer
    
    Symmetric Encryption
    
    Public Key Cryptography
    
    Hash Functions
    
    MAC Functions
    
    Random Number Generation
    
    Provider Framework
    
    Default Provider
    
    Hardware-optimized Implementations
    
    Custom Providers
    
    CRYPT_EAL_CipherCtx
    
    Cipher Operations
    
    Init
    
    Update
    
    Final
    
    Padding

Sources:
[crypto/provider/src/mgr/crypt_provider.c35-135](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c#L35-L135)
[testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c65-175](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c#L65-L175)

## API Interface

The symmetric encryption API is designed to be straightforward and flexible.
It follows the common pattern of context initialization, update, and
finalization.

### Core Data Structures

The main context structure used for symmetric encryption operations is
`CRYPT_EAL_CipherCtx`, which encapsulates all the state information needed for
encryption and decryption operations.

### Core Functions

The following functions form the core of the symmetric encryption API:

#### Context Management

Function| Description  
---|---  
`CRYPT_EAL_CipherNewCtx(int algId)`| Creates a new cipher context for the
specified algorithm  
`CRYPT_EAL_CipherFreeCtx(CRYPT_EAL_CipherCtx *ctx)`| Frees the resources
associated with the cipher context  
`CRYPT_EAL_CipherDeinit(CRYPT_EAL_CipherCtx *ctx)`| Cleans up the cipher
context but doesn't free it  
  
#### Encryption/Decryption Operations

Function| Description  
---|---  
`CRYPT_EAL_CipherInit(ctx, key, keyLen, iv, ivLen, encrypt)`| Initializes the
cipher context with key, initialization vector (IV), and operation mode  
`CRYPT_EAL_CipherReinit(ctx, iv, ivLen)`| Reinitializes the cipher context
with a new IV  
`CRYPT_EAL_CipherUpdate(ctx, in, inLen, out, outLen)`| Processes a chunk of
data, can be called multiple times  
`CRYPT_EAL_CipherFinal(ctx, out, outLen)`| Finalizes the encryption/decryption
operation, processes any remaining data  
  
#### Additional Settings

Function| Description  
---|---  
`CRYPT_EAL_CipherSetPadding(ctx, padding)`| Sets the padding mode (e.g.,
PKCS7, ISO, ANSI X.923)  
`CRYPT_EAL_CipherCtrl(ctx, cmd, val, valLen)`| Sets various cipher parameters
and controls  
  
Sources:
[testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c85-147](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c#L85-L147)
[docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application
Development
Guide.md24-175](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/1_Encryption and Integrity Protection Application Development
Guide.md#L24-L175)

### API Flow

The typical flow for using the symmetric encryption API is as follows:

    
    
    "Provider Framework""Cipher API""Application""Provider Framework""Cipher API""Application"loop[For each data chunk]CRYPT_EAL_CipherNewCtx(CRYPT_CIPHER_*)Select implementationReturn implementationReturn contextCRYPT_EAL_CipherInit(ctx, key, key_len, iv, iv_len, true/false)Initialize cipher with key and IVSuccess/FailureStatus codeCRYPT_EAL_CipherSetPadding(ctx, CRYPT_PADDING_*)Configure paddingSuccess/FailureStatus codeCRYPT_EAL_CipherUpdate(ctx, in_data, in_len, out_data, &out_len)Process data chunkProcessed dataProcessed data + lengthCRYPT_EAL_CipherFinal(ctx, final_out, &final_len)Process final block with paddingFinal processed dataFinal data + lengthCRYPT_EAL_CipherFreeCtx(ctx)Clean up resourcesSuccessVoid

Sources:
[testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c33-63](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c#L33-L63)
[docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application
Development
Guide.md24-175](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/1_Encryption and Integrity Protection Application Development
Guide.md#L24-L175)

## Usage Example

The following is a basic example of using AES-CBC for encryption and
decryption:

    
    
    // Create a context for AES-CBC
    CRYPT_EAL_CipherCtx *ctx = CRYPT_EAL_CipherNewCtx(CRYPT_CIPHER_AES128_CBC);
    if (ctx == NULL) {
        // Handle error
        return 1;
    }
    
    // Initialize for encryption with key and IV
    ret = CRYPT_EAL_CipherInit(ctx, key, keyLen, iv, ivLen, true);
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        goto EXIT;
    }
    
    // Set padding mode
    ret = CRYPT_EAL_CipherSetPadding(ctx, CRYPT_PADDING_PKCS7);
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        goto EXIT;
    }
    
    // Encrypt data
    ret = CRYPT_EAL_CipherUpdate(ctx, plaintext, plaintextLen, ciphertext, &outLen);
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        goto EXIT;
    }
    totalLen = outLen;
    
    // Finalize encryption
    ret = CRYPT_EAL_CipherFinal(ctx, ciphertext + totalLen, &outLen);
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        goto EXIT;
    }
    totalLen += outLen;
    
    // Reinitialize for decryption
    ret = CRYPT_EAL_CipherInit(ctx, key, keyLen, iv, ivLen, false);
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        goto EXIT;
    }
    
    // Set the same padding mode for decryption
    ret = CRYPT_EAL_CipherSetPadding(ctx, CRYPT_PADDING_PKCS7);
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        goto EXIT;
    }
    
    // Decrypt data
    ret = CRYPT_EAL_CipherUpdate(ctx, ciphertext, totalLen, decrypted, &outLen);
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        goto EXIT;
    }
    decryptedLen = outLen;
    
    // Finalize decryption
    ret = CRYPT_EAL_CipherFinal(ctx, decrypted + decryptedLen, &outLen);
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        goto EXIT;
    }
    decryptedLen += outLen;
    
    EXIT:
    // Clean up
    CRYPT_EAL_CipherFreeCtx(ctx);

Sources: [docs/en/5_Developer Guide/1_Encryption and Integrity Protection
Application Development
Guide.md24-175](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/1_Encryption and Integrity Protection Application Development
Guide.md#L24-L175)

## Implementation Details

### Provider Framework Integration

The symmetric encryption capabilities are integrated with the provider
framework, allowing different implementations to be used based on availability
and performance requirements. The provider framework enables:

  1. Hardware-accelerated implementations when available
  2. Optimized assembly implementations for specific platforms
  3. Custom provider implementations for specialized use cases

    
    
    CRYPT_EAL_Cipher API
    
    Provider Framework
    
    Default Provider
    
    Custom Providers
    
    AES Software Implementation
    
    AES Assembly Optimized
    
    AES-NI Hardware Acceleration
    
    SM4 Implementation
    
    ChaCha20 Implementation
    
    Hardware Security Module
    
    PKCS#11 Module
    
    Custom Implementations
    
    Application

Sources:
[crypto/provider/src/mgr/crypt_provider.c35-100](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c#L35-L100)
[crypto/provider/include/crypt_provider.h15-65](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h#L15-L65)

### Assembly Optimizations

The library includes assembly-optimized implementations for various algorithms
and platforms to maximize performance:

Algorithm| Platform| Optimization| Define  
---|---|---|---  
AES| x86_64| AES-NI Instructions| HITLS_CRYPTO_AES_X8664  
AES| ARMv8| Crypto Extensions| HITLS_CRYPTO_AES_ARMV8  
ChaCha20| x86_64| SIMD Instructions| HITLS_CRYPTO_CHACHA20_X8664  
ChaCha20| ARMv8| NEON/SVE| HITLS_CRYPTO_CHACHA20_ARMV8  
SM4| x86_64| SIMD Instructions| HITLS_CRYPTO_SM4_X8664  
SM4| ARMv8| NEON/SVE| HITLS_CRYPTO_SM4_ARMV8  
GCM| x86_64| SIMD Instructions| HITLS_CRYPTO_GCM_X8664  
GCM| ARMv8| NEON/SVE| HITLS_CRYPTO_GCM_ARMV8  
  
The assembly optimizations are automatically enabled during compilation if the
target platform supports them.

Sources:
[config/macro_config/hitls_config_layer_crypto.h669-702](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L669-L702)

### Memory Considerations

The library offers memory-optimized versions of some algorithms for
constrained environments:

    
    
    // Small memory footprint versions
    #ifdef HITLS_CRYPTO_AES_SMALL_MEM
    // Uses less tables but slightly slower
    #endif
    
    #ifdef HITLS_CRYPTO_SHA256_SMALL_MEM
    // Uses less tables but slightly slower
    #endif

Sources:
[config/macro_config/hitls_config_layer_crypto.h51-55](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L51-L55)
[crypto/aes/src/crypt_aes_tbox.c50-61](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c#L50-L61)

## AEAD Modes

Authenticated Encryption with Associated Data (AEAD) modes provide both
confidentiality and authenticity. openHiTLS supports several AEAD modes:

### GCM (Galois/Counter Mode)

GCM combines the counter mode of encryption with the Galois mode of
authentication. The API for GCM includes additional functions for setting the
authentication tag and the associated data:

    
    
    // Set authentication data (optional, must be called before Update)
    ret = CRYPT_EAL_CipherCtrl(ctx, CRYPT_CTRL_SET_GCM_AAD, aad, aadLen);
    
    // For decryption, set the expected tag (must be called before Final)
    ret = CRYPT_EAL_CipherCtrl(ctx, CRYPT_CTRL_SET_GCM_TAG, tag, tagLen);
    
    // For encryption, get the authentication tag after Final
    ret = CRYPT_EAL_CipherCtrl(ctx, CRYPT_CTRL_GET_GCM_TAG, tag, &tagLen);

### CCM (Counter with CBC-MAC)

CCM combines the counter mode for encryption with CBC-MAC for authentication.
The API is similar to GCM but requires setting the payload length before
starting the encryption:

    
    
    // Set the total plaintext length (must be called before Update)
    ret = CRYPT_EAL_CipherCtrl(ctx, CRYPT_CTRL_SET_CCM_PLAINTEXT_LEN, &plaintextLen, sizeof(plaintextLen));
    
    // Set authentication data (optional, must be called before Update)
    ret = CRYPT_EAL_CipherCtrl(ctx, CRYPT_CTRL_SET_CCM_AAD, aad, aadLen);

### ChaCha20Poly1305

ChaCha20Poly1305 combines the ChaCha20 stream cipher with the Poly1305 message
authentication code. The API is similar to GCM:

    
    
    // Set authentication data (optional, must be called before Update)
    ret = CRYPT_EAL_CipherCtrl(ctx, CRYPT_CTRL_SET_CHACHA20POLY1305_AAD, aad, aadLen);
    
    // For decryption, set the expected tag (must be called before Final)
    ret = CRYPT_EAL_CipherCtrl(ctx, CRYPT_CTRL_SET_CHACHA20POLY1305_TAG, tag, tagLen);
    
    // For encryption, get the authentication tag after Final
    ret = CRYPT_EAL_CipherCtrl(ctx, CRYPT_CTRL_GET_CHACHA20POLY1305_TAG, tag, &tagLen);

## Error Handling

The symmetric encryption API uses return codes to indicate success or failure.
The common error codes include:

Error Code| Description  
---|---  
CRYPT_SUCCESS| Operation completed successfully  
CRYPT_NULL_INPUT| One or more required input parameters is NULL  
CRYPT_INVALID_ARG| Invalid argument provided  
CRYPT_AES_ERR_KEYLEN| Invalid key length for the specified algorithm  
CRYPT_MODES_IVLEN_ERROR| Invalid initialization vector length  
CRYPT_EAL_ERR_PART_OVERLAP| Input and output buffers partially overlap  
CRYPT_MEM_ALLOC_FAIL| Memory allocation failure  
  
The library also supports detailed error tracking using the BSL_ERR module,
which can help identify the exact function and line where an error occurred.

## Performance Considerations

When using symmetric encryption, consider the following performance aspects:

  1. **Hardware Acceleration** : Use hardware-accelerated implementations when available for best performance.
  2. **Buffer Management** : Avoid excessive reallocation by pre-allocating buffers of appropriate size.
  3. **Algorithm Choice** : AES-GCM with hardware acceleration is typically the fastest AEAD mode on modern platforms.
  4. **Block Size** : Process data in multiples of the block size when possible to avoid padding overhead.
  5. **Assembly Optimizations** : Enable assembly optimizations during compilation for target platforms.

The symmetric encryption implementation in openHiTLS is designed to balance
security, performance, and resource usage across a wide range of deployment
scenarios.

# Key and Certificate Handling

Relevant source files

  * [bsl/asn1/src/bsl_asn1_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/asn1/src/bsl_asn1_local.h)
  * [bsl/pem/include/bsl_pem_internal.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/pem/include/bsl_pem_internal.h)
  * [bsl/pem/src/bsl_pem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/pem/src/bsl_pem.c)
  * [bsl/sal/src/sal_file.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/sal/src/sal_file.c)
  * [crypto/curve25519/src/curve25519.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/curve25519/src/curve25519.c)
  * [crypto/dh/src/dh_core.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/dh/src/dh_core.c)
  * [crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)
  * [crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
  * [crypto/ecc/src/ecc_pkey.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecc_pkey.c)
  * [crypto/ecc/src/ecp_mont.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecp_mont.c)
  * [crypto/encode/src/crypt_encode.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/encode/src/crypt_encode.c)
  * [crypto/hybridkem/src/crypt_hybridkem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c)
  * [crypto/hybridkem/src/crypt_hybridkem_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem_local.h)
  * [crypto/mldsa/src/ml_dsa.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/mldsa/src/ml_dsa.c)
  * [crypto/provider/src/default/crypt_default_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c)
  * [crypto/sm2/src/sm2_crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sm2/src/sm2_crypt.c)
  * [include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)
  * [include/crypto/crypt_params_key.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_params_key.h)
  * [pki/x509_common/src/hitls_x509_common.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/pki/x509_common/src/hitls_x509_common.c)
  * [testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c)
  * [testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.data)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data)
  * [testcode/sdv/testcase/crypto/encode/test_suite_sdv_asn1_certkey.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/encode/test_suite_sdv_asn1_certkey.c)
  * [testcode/sdv/testcase/crypto/encode/test_suite_sdv_asn1_certkey.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/encode/test_suite_sdv_asn1_certkey.data)
  * [testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_api.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_api.c)
  * [testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_api.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_api.data)
  * [testcode/testdata/provider/provider_get_cap_test1.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/testdata/provider/provider_get_cap_test1.c)
  * [tls/crypt/crypt_self/hitls_crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_self/hitls_crypt.c)

This page documents the key and certificate handling systems within the
openHiTLS project. It covers how cryptographic keys and certificates are
encoded, decoded, and managed throughout the library. For information about
public key cryptography operations, see [Public Key
Cryptography](/openHiTLS/openHiTLS/3.2-public-key-cryptography), and for
random number generation (which is used in key generation), see [Random Number
Generation](/openHiTLS/openHiTLS/3.1-random-number-generation).

## Overview

The key and certificate handling subsystem provides infrastructure for:

  1. Creating, storing, and managing cryptographic keys of various types
  2. Encoding and decoding keys in different formats (raw binary, ASN.1, PEM)
  3. Parameter management for different key types
  4. Certificate handling including parsing and validation
  5. Support for both traditional and post-quantum cryptographic keys

The system is designed to be extensible, supporting multiple key types through
a unified interface while allowing algorithm-specific operations.

    
    
    Application
    
    Key Management API
    
    Key Generation
    
    Key Import/Export
    
    Parameter Management
    
    Certificate Operations
    
    CRYPT_EAL_PkeyGen
    
    CRYPT_EAL_PkeyGetPub/GetPrv
    
    CRYPT_EAL_PkeySetPub/SetPrv
    
    CRYPT_EAL_PkeySetPara/GetPara
    
    ASN.1/PEM Encoding/Decoding
    
    Key Context
    
    Public Key
    
    Private Key
    
    Certificate Parsing
    
    Key Format Conversion

Sources:
[crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
[include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)

## Key Data Structures

The key handling system defines unified structures to represent different
types of keys. These structures are organized in unions to provide a common
interface across different key algorithms.

### Key Type Hierarchy

    
    
    CRYPT_EAL_PkeyCtx
    
    +key: void
    
    +method: EAL_PkeyUnitaryMethod
    
    +id: CRYPT_PKEY_AlgId
    
    +references: BSL_SAL_RefCount
    
    CRYPT_EAL_PkeyPub
    
    +id: CRYPT_PKEY_AlgId
    
    +key: union
    
    CRYPT_EAL_PkeyPrv
    
    +id: CRYPT_PKEY_AlgId
    
    +key: union
    
    CRYPT_EAL_PkeyPara
    
    +id: CRYPT_PKEY_AlgId
    
    +para: union
    
    RSAPub
    
    DSAPub
    
    DHPub
    
    ECCPub
    
    Curve25519Pub
    
    PaillierPub
    
    KemEncapsKey
    
    ElGamalPub
    
    RSAPrv
    
    DSAPrv
    
    DHPrv
    
    ECCPrv
    
    Curve25519Prv
    
    PaillierPrv
    
    KemDecapsKey
    
    ElGamalPrv

Sources:
[include/crypto/crypt_eal_pkey.h40-81](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L40-L81)

### Key Parameter Management

The system uses a parameterized approach to handle key-specific data.
Parameters are identified by unique values defined in `crypt_params_key.h`.

Parameter Base| Purpose| Example Parameters  
---|---|---  
CRYPT_PARAM_PKEY_BASE| Generic public key parameters|
CRYPT_PARAM_PKEY_ENCODE_PUBKEY  
CRYPT_PARAM_EC_BASE| Elliptic curve parameters|
CRYPT_PARAM_EC_POINT_UNCOMPRESSED, CRYPT_PARAM_EC_PRVKEY  
CRYPT_PARAM_DH_BASE| Diffie-Hellman parameters| CRYPT_PARAM_DH_PUBKEY,
CRYPT_PARAM_DH_P  
CRYPT_PARAM_RSA_BASE| RSA parameters| CRYPT_PARAM_RSA_N, CRYPT_PARAM_RSA_E  
CRYPT_PARAM_CURVE25519_BASE| X25519/ED25519 parameters|
CRYPT_PARAM_CURVE25519_PUBKEY  
CRYPT_PARAM_ML_KEM_BASE| Post-quantum KEM parameters|
CRYPT_PARAM_ML_KEM_PUBKEY  
CRYPT_PARAM_HYBRID_BASE| Hybrid cryptography parameters|
CRYPT_PARAM_HYBRID_PUBKEY  
  
Sources:
[include/crypto/crypt_params_key.h26-141](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_params_key.h#L26-L141)

## Key Context Management

Keys are managed through context objects that encapsulate the key data and
associated methods.

    
    
    Algorithm MethodsCRYPT_EAL_PkeyCtxKey APIApplicationAlgorithm MethodsCRYPT_EAL_PkeyCtxKey APIApplicationCRYPT_EAL_PkeyNewCtx(algId)Create new contextFind method for algorithmReturn methodAssign methodReturn key contextCRYPT_EAL_PkeyGen(ctx)Access methodCall generation functionStore generated keySuccess/ErrorSuccess/ErrorCRYPT_EAL_PkeyGetPub/GetPrvAccess methodCall export functionReturn key dataKey dataCRYPT_EAL_PkeyFreeCtx(ctx)Decrease reference countCall cleanup if ref count = 0Resources freedSuccess

Sources:
[crypto/eal/src/eal_pkey_gen.c70-206](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L70-L206)

### Reference Counting

The key context implements reference counting to manage key lifetimes:

    
    
    int ref = 0;
    BSL_SAL_AtomicDownReferences(&(pkey->references), &ref);
    if (ref > 0) {
        return;
    }

Sources:
[crypto/eal/src/eal_pkey_gen.c196-199](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L196-L199)

## Key Generation

Key generation is handled through a consistent interface regardless of key
type.

    
    
    RSA
    
    ECDSA/ECDH
    
    DH
    
    X25519/ED25519
    
    Hybrid
    
    Post-quantum
    
    CRYPT_EAL_PkeyGen(pkey)
    
    Validate input
    
    Algorithm-specific generation
    
    RSA Key Generation
    
    EC Key Generation
    
    DH Key Generation
    
    Curve25519 Key Generation
    
    Hybrid Key Generation
    
    PQ Key Generation
    
    Key generation result
    
    Report event to logging system
    
    Return success/error

Sources:
[crypto/eal/src/eal_pkey_gen.c483-504](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L483-L504)

### Entropy for Key Generation

Key generation relies on strong entropy sourced from the DRBG (Deterministic
Random Bit Generator) subsystem, which provides cryptographically secure
random numbers.

    
    
    Key Generation Request
    
    CRYPT_EAL_PkeyGen
    
    Algorithm-specific gen method
    
    Request entropy from DRBG
    
    DRBG_GetEntropy
    
    Generate key components
    
    Assemble key pair
    
    Return generated key

Sources:
[crypto/drbg/src/drbg.c57-98](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c#L57-L98)

## Setting and Getting Keys

The library provides functions to set and retrieve key components:

### Public Key Operations

    
    
    int32_t CRYPT_EAL_PkeySetPub(CRYPT_EAL_PkeyCtx *pkey, const CRYPT_EAL_PkeyPub *key);
    int32_t CRYPT_EAL_PkeyGetPub(const CRYPT_EAL_PkeyCtx *pkey, CRYPT_EAL_PkeyPub *key);

### Private Key Operations

    
    
    int32_t CRYPT_EAL_PkeySetPrv(CRYPT_EAL_PkeyCtx *pkey, const CRYPT_EAL_PkeyPrv *key);
    int32_t CRYPT_EAL_PkeyGetPrv(const CRYPT_EAL_PkeyCtx *pkey, CRYPT_EAL_PkeyPrv *key);

Each key type implements specific logic for setting and retrieving key data
based on its format.

Sources:
[crypto/eal/src/eal_pkey_gen.c532-753](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L532-L753)
[crypto/eal/src/eal_pkey_gen.c950-1031](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L950-L1031)

### Extended Key Operations

For more complex key operations, the library provides extended functions that
work with parameter lists:

    
    
    int32_t CRYPT_EAL_PkeySetPubEx(CRYPT_EAL_PkeyCtx *pkey, const BSL_Param *param);
    int32_t CRYPT_EAL_PkeyGetPubEx(const CRYPT_EAL_PkeyCtx *pkey, BSL_Param *param);
    int32_t CRYPT_EAL_PkeySetPrvEx(CRYPT_EAL_PkeyCtx *pkey, const BSL_Param *param);
    int32_t CRYPT_EAL_PkeyGetPrvEx(const CRYPT_EAL_PkeyCtx *pkey, BSL_Param *param);

Sources:
[crypto/eal/src/eal_pkey_gen.c817-891](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L817-L891)

## Supported Key Types

The library supports a wide range of key types for different cryptographic
algorithms:

Key Type| Description| Public Key Structure| Private Key Structure  
---|---|---|---  
RSA| Traditional asymmetric cryptography| CRYPT_RsaPub| CRYPT_RsaPrv  
DSA| Digital Signature Algorithm| CRYPT_DsaPub| CRYPT_DsaPrv  
DH| Diffie-Hellman key exchange| CRYPT_DhPub| CRYPT_DhPrv  
ECDSA/ECDH| Elliptic Curve cryptography| CRYPT_EccPub| CRYPT_EccPrv  
ED25519/X25519| Edwards/Montgomery curve| CRYPT_Curve25519Pub|
CRYPT_Curve25519Prv  
SM2| Chinese cryptography standard| CRYPT_EccPub| CRYPT_EccPrv  
ML-KEM| Post-quantum KEM| CRYPT_KemEncapsKey| CRYPT_KemDecapsKey  
Hybrid KEM| Classical + Post-quantum| CRYPT_KemEncapsKey| CRYPT_KemDecapsKey  
  
Sources:
[include/crypto/crypt_eal_pkey.h40-81](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h#L40-L81)

### Hybrid Key Handling

The library has special support for hybrid cryptography, which combines
classical (e.g., ECDH or X25519) with post-quantum algorithms for enhanced
security.

    
    
    CRYPT_HYBRID_KEM_GenKey
    
    Generate classical key
    
    Generate post-quantum key
    
    Combined hybrid key
    
    CRYPT_HYBRID_KEM_Encaps
    
    Classical encapsulation
    
    PQ encapsulation
    
    Combined shared secret
    
    CRYPT_HYBRID_KEM_Decaps
    
    Classical decapsulation
    
    PQ decapsulation
    
    Recovered shared secret

Sources:
[crypto/hybridkem/src/crypt_hybridkem.c278-470](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c#L278-L470)
[crypto/hybridkem/src/crypt_hybridkem_local.h22-29](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem_local.h#L22-L29)

## Key Parameter Handling

Parameters for various key types are managed through a unified interface:

    
    
    RSA
    
    DSA
    
    DH
    
    EC
    
    Others
    
    CRYPT_EAL_PkeySetPara
    
    Validate parameters
    
    Algorithm-specific parameter setting
    
    Set RSA parameters
    
    Set DSA parameters
    
    Set DH parameters
    
    Set EC parameters
    
    Set other parameters
    
    Parameter result
    
    Return success/error

Sources:
[crypto/eal/src/eal_pkey_gen.c356-389](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L356-L389)
[crypto/eal/src/eal_pkey_gen.c420-458](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L420-L458)

### Example: Setting DH Parameters

    
    
    static int32_t SetDhParams(CRYPT_EAL_PkeyCtx *pkey, const CRYPT_DhPara *dhPara)
    {
        BSL_Param param[4] = {
            {CRYPT_PARAM_DH_P, BSL_PARAM_TYPE_OCTETS, dhPara->p, dhPara->pLen, 0},
            {CRYPT_PARAM_DH_Q, BSL_PARAM_TYPE_OCTETS, dhPara->q, dhPara->qLen, 0},
            {CRYPT_PARAM_DH_G, BSL_PARAM_TYPE_OCTETS, dhPara->g, dhPara->gLen, 0},
            BSL_PARAM_END
        };
        return pkey->method->setPara(pkey->key, param);
    }

Sources:
[crypto/eal/src/eal_pkey_gen.c246-255](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L246-L255)

## Key Format and Encoding

Keys can be represented in various formats:

  1. **Raw binary format** : Direct memory representation of key components
  2. **ASN.1 format** : Structured encoding for certificate and key storage
  3. **PEM format** : Base64-encoded ASN.1 with header/footer for text representation

    
    
    ASN.1 Encode
    
    Base64 Encode + Headers
    
    Parse + Base64 Decode
    
    ASN.1 Decode
    
    Raw Key Data
    
    ASN.1 DER Format
    
    PEM Format
    
    ASN.1 DER Format
    
    Raw Key Data

Sources:
[bsl/pem/src/bsl_pem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/pem/src/bsl_pem.c)
[crypto/encode/src/crypt_encode.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/encode/src/crypt_encode.c)

### PEM Format Handling

The library parses PEM-formatted keys using header and footer markers:

    
    
    bool BSL_PEM_IsPemFormat(const char *buff, uint32_t len);
    int32_t BSL_PEM_DecodePemToAsn1(char **pemdata, uint32_t *len, const BSL_PEM_Symbol *sym, 
                                   uint8_t **asn1Encode, uint32_t *asn1Len);

Example PEM header and footer for EC private keys:

    
    
    -----BEGIN EC PRIVATE KEY-----
    ...base64-encoded data...
    -----END EC PRIVATE KEY-----
    

Sources:
[testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c67-80](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c#L67-L80)

### ASN.1 Template for RSA Private Keys

    
    
    BSL_ASN1_TemplateItem rsaPrvTempl[] = {
     {BSL_ASN1_TAG_CONSTRUCTED | BSL_ASN1_TAG_SEQUENCE, 0, 0}, /* seq */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* version */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* n */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* e */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* d */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* p */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* q */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* d mod (p-1) */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* d mod (q-1) */
      {BSL_ASN1_TAG_INTEGER, 0, 1}, /* q^-1 mod p */
      // Optional fields for multi-prime RSA
    };

Sources:
[testcode/sdv/testcase/crypto/encode/test_suite_sdv_asn1_certkey.c50-67](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/encode/test_suite_sdv_asn1_certkey.c#L50-L67)

## Certificate Handling

Certificate parsing and validation builds on the key handling infrastructure.

    
    
    X.509 Certificate
    
    Parse ASN.1 Structure
    
    Extract TBS Certificate
    
    Parse Certificate Fields
    
    Extract Subject
    
    Extract Issuer
    
    Extract Validity Period
    
    Extract Public Key
    
    Extract Extensions
    
    Extract Signature Algorithm
    
    Extract Signature Value
    
    Parse Public Key Info
    
    Identify Key Algorithm
    
    Extract Key Parameters
    
    Create Public Key Structure

Sources:
[pki/x509_common/src/hitls_x509_common.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/pki/x509_common/src/hitls_x509_common.c)

### Certificate Raw Data Parsing

The library extracts the TBS (To Be Signed) portion of X.509 certificates:

    
    
    int32_t HITLS_X509_ParseTbsRawData(uint8_t *encode, uint32_t encodeLen, 
                                     uint8_t **tbsRawData, uint32_t *tbsRawDataLen)
    {
        uint8_t *temp = encode;
        uint32_t tempLen = encodeLen;
        uint32_t valLen;
        // Parse outer SEQUENCE
        int32_t ret = BSL_ASN1_DecodeTagLen(BSL_ASN1_TAG_CONSTRUCTED | BSL_ASN1_TAG_SEQUENCE, 
                                            &temp, &tempLen, &valLen);
        // ... more processing ...
        
        *tbsRawData = temp;
        *tbsRawDataLen = len - tempLen + valLen;
        return ret;
    }

Sources:
[pki/x509_common/src/hitls_x509_common.c55-77](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/pki/x509_common/src/hitls_x509_common.c#L55-L77)

## Integration with TLS

The key and certificate handling subsystem integrates with the TLS protocol
implementation for secure communications.

    
    
    TLS Protocol Layer
    
    Handshake Protocol
    
    Certificate Message
    
    X.509 Certificate Parsing
    
    Public Key Extraction
    
    Key Exchange
    
    Key Generation
    
    Key Encapsulation
    
    Derive Session Keys

Sources:
[tls/crypt/crypt_self/hitls_crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_self/hitls_crypt.c)

## Error Handling

The key and certificate handling subsystem uses a consistent error reporting
mechanism:

    
    
    if (ret != CRYPT_SUCCESS) {
        BSL_ERR_PUSH_ERROR(ret);
        return ret;
    }

For key-related operations, event reporting is also utilized:

    
    
    EAL_EventReport(CRYPT_EVENT_GEN, CRYPT_ALGO_PKEY, pkey->id, CRYPT_SUCCESS);

Sources:
[crypto/eal/src/eal_pkey_gen.c502-503](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c#L502-L503)

## Summary

The key and certificate handling subsystem provides a comprehensive framework
for managing cryptographic keys and certificates in openHiTLS. It supports:

  1. Multiple key types, including traditional and post-quantum algorithms
  2. Unified interface for key operations
  3. Flexible parameter system for algorithm-specific settings
  4. Certificate parsing and validation
  5. Various encoding formats (raw, ASN.1, PEM)
  6. Integration with other subsystems like TLS and random number generation

The design emphasizes extensibility, security, and usability while maintaining
compatibility with cryptographic standards.

# TLS Protocol Implementation

Relevant source files

  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [config/macro_config/hitls_config_check.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_check.h)
  * [config/macro_config/hitls_config_layer_tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_tls.h)
  * [crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
  * [crypto/provider/src/default/crypt_default_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c)
  * [include/tls/hitls_config.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h)
  * [include/tls/hitls_crypt_type.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_crypt_type.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/demo/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt)
  * [testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
  * [testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c)
  * [testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)
  * [testcode/demo/privpass_token.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c)
  * [testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
  * [testcode/demo/sm2enc.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c)
  * [testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/framework/tls/rpc/src/hitls_func.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/rpc/src/hitls_func.c)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c)
  * [tls/config/src/cipher_suite.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/cipher_suite.c)
  * [tls/config/src/config_default.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_default.c)
  * [tls/config/src/config_group.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c)
  * [tls/crypt/crypt_adapt/crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_adapt/crypt.c)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_ctx.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_ctx.h)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/common/src/hs_kx.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
  * [tls/handshake/pack/src/pack_hello_verify_request.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_hello_verify_request.c)
  * [tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)
  * [tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)
  * [tls/record/src/rec_write.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c)

This document describes the Transport Layer Security (TLS) protocol
implementation in the openHiTLS project. The TLS Protocol Layer serves as the
core component that ensures secure communication over networks by providing
encryption, authentication, and integrity protection services.

For information about using PKI/X.509 functionality, see [Key and Certificate
Handling](/openHiTLS/openHiTLS/3.4-key-and-certificate-handling). For details
about building and integrating openHiTLS, see [Building and
Configuration](/openHiTLS/openHiTLS/5-building-and-configuration).

## Architecture Overview

The TLS Protocol Implementation follows a layered architecture with the TLS
Protocol Layer sitting between applications and the Cryptographic Services
Layer:

    
    
    TLS Protocol Layer
    
    Applications
    
    TLS Protocol Layer
    
    Cryptographic Services Layer
    
    Provider Framework
    
    Handshake Protocol
    
    Record Protocol
    
    Alert Protocol
    
    Configuration

Sources:
[config/json/feature.json222-583](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L222-L583)

The core components of the TLS protocol implementation work together to
establish and maintain secure connections:

    
    
    HITLS_Ctx
    
    Handshake Context (hsCtx)
    
    Record Context (recCtx)
    
    Configuration (config)
    
    I/O Handling (uio)
    
    KeyExchCtx
    
    Extension Flags
    
    Transcript Hash
    
    Write States
    
    Read States
    
    Crypto Operations
    
    Protocol Versions
    
    Cipher Suites
    
    Key Exchange Groups
    
    Extensions

Sources:
[tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
[tls/handshake/common/include/hs_ctx.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_ctx.h)

## Protocol Versions

The TLS Protocol Implementation supports multiple protocol versions:

Protocol Version| Identifier| Description  
---|---|---  
TLS 1.2| 0x0303| Transport Layer Security v1.2  
TLS 1.3| 0x0304| Transport Layer Security v1.3  
DTLS 1.2| 0xFEFD| Datagram Transport Layer Security v1.2  
TLCP 1.1| 0x0101| Chinese standard protocol based on TLS  
  
Sources:
[include/tls/hitls_config.h38-71](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h#L38-L71)
[config/json/feature.json226-231](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L226-L231)

## Handshake Protocol

The Handshake Protocol establishes the secure connection by negotiating
parameters and exchanging keys:

    
    
    ServerClientServerClientTLS 1.2 HandshakeTLS 1.3 HandshakeClientHelloServerHelloCertificateServerKeyExchangeServerHelloDoneClientKeyExchangeChangeCipherSpecFinishedChangeCipherSpecFinishedClientHello + KeyShareServerHello + KeyShare{EncryptedExtensions}{Certificate}{CertificateVerify}{Finished}{Finished}

Sources:
[tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)
[tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)

### Key Exchange Mechanisms

The implementation supports various key exchange mechanisms:

    
    
    Key Exchange
    
    RSA Key Transport
    
    ECDHE
    
    DHE
    
    PSK
    
    NIST Curves
    
    Edwards Curves
    
    Brainpool Curves
    
    SM2 Curves
    
    DH Parameter Generation
    
    DH Key Agreement

Sources:
[tls/handshake/common/src/hs_kx.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c)
[testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)

Key exchange operations are implemented in the `KeyExchCtx` structure, which
manages algorithms including:

  * **RSA** : Client encrypts pre-master secret with server's public key
  * **ECDHE** : Ephemeral ECDH key pairs for forward secrecy
  * **DHE** : Ephemeral DH key pairs for forward secrecy
  * **PSK** : Pre-shared key authentication and key derivation

The key exchange implementation handles both client-side operations
(generating key pairs, processing server key exchange messages) and server-
side operations (generating key pairs, processing client key exchange
messages).

Sources:
[tls/handshake/common/src/hs_kx.c38-256](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L38-L256)

### Extension Handling

The TLS implementation supports numerous extensions that enhance the base
protocol:

    
    
    Extensions
    
    Server Name Indication (SNI)
    
    Signature Algorithms
    
    Supported Groups
    
    Key Share
    
    Pre-shared Key (PSK)
    
    ALPN
    
    Session Ticket
    
    Extended Master Secret
    
    Point Formats

The extension handling system:

  1. Packs extensions in outgoing messages
  2. Parses extensions in incoming messages
  3. Processes extension data to affect handshake behavior

Sources:
[tls/handshake/pack/src/pack_extensions.c52-179](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L52-L179)

## Record Protocol

The Record Protocol is responsible for encapsulating, protecting, and
transmitting TLS data:

    
    
    Record Protocol
    
    Record Writing
    
    Record Reading
    
    Record Crypto
    
    Fragmentation
    
    Encryption
    
    MAC/AEAD
    
    Decryption
    
    Verification
    
    Reassembly
    
    Cipher Suite Implementation
    
    Key Management
    
    Sequence Number Handling

Sources:
[tls/record/src/rec_write.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c)

The Record Protocol maintains separate connection states for reading and
writing, each containing:

  * Protocol version
  * Cipher suite information
  * Cryptographic keys
  * Sequence numbers
  * MAC secrets (for non-AEAD ciphers)

The `RecCtx` structure manages these states and provides functions to:

  * Write application data as encrypted TLS records
  * Read and decrypt TLS records into application data
  * Handle content type distinction (application data, handshake, alerts)
  * Manage protection against attacks (padding, timing, etc.)

Sources:
[tls/record/src/rec_write.c38-54](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L38-L54)

## Cipher Suites

The implementation supports a wide range of cipher suites:

Protocol| Example Cipher Suites  
---|---  
TLS 1.2| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384  
TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256  
TLS 1.3| TLS_AES_128_GCM_SHA256  
TLS_AES_256_GCM_SHA384  
TLS_CHACHA20_POLY1305_SHA256  
  
Sources:
[config/json/feature.json291-553](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L291-L553)
[tls/config/src/cipher_suite.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/cipher_suite.c)

The cipher suite configuration dictates:

  * The key exchange algorithm
  * The authentication mechanism
  * The bulk encryption algorithm and mode
  * The message authentication code (MAC) algorithm or AEAD construction
  * The pseudo-random function (PRF) used for key derivation

## Alert Protocol

The Alert Protocol handles error conditions and notifications:

    
    
    Alert Protocol
    
    Warning Alerts
    
    Fatal Alerts
    
    close_notify
    
    user_canceled
    
    unexpected_message
    
    bad_record_mac
    
    handshake_failure
    
    bad_certificate
    
    decrypt_error

Sources:
[include/tls/hitls_error.h81-174](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L81-L174)

Alerts are categorized as:

  * **Warning (level 1)** : May allow the connection to continue
  * **Fatal (level 2)** : Immediately terminate the connection

Each alert has a specific meaning, such as `bad_certificate` indicating a
certificate validation issue or `decrypt_error` indicating a failure in
decryption.

## Client Implementation

The client-side implementation initiates the TLS handshake and handles:

    
    
    Client TLS Implementation
    
    Initialize TLS Library
    
    Create and Configure TLS Context
    
    Set Up I/O
    
    Establish TLS Connection
    
    Exchange Application Data
    
    Close TLS Connection

Sources:
[testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)

Example client usage:

    
    
    // Initialize cryptographic library
    CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
    CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Configure TLS
    HITLS_Config *config = HITLS_CFG_NewTLS12Config();
    HITLS_X509_CertParseFile(BSL_FORMAT_ASN1, "ca.der", &rootCA);
    HITLS_CFG_AddCertToStore(config, rootCA, TLS_CERT_STORE_TYPE_DEFAULT, true);
    
    // Create TLS context
    HITLS_Ctx *ctx = HITLS_New(config);
    
    // Set up I/O
    uio = BSL_UIO_New(BSL_UIO_TcpMethod());
    BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, sizeof(fd), &fd);
    HITLS_SetUio(ctx, uio);
    
    // Connect, exchange data, and close
    HITLS_Connect(ctx);
    HITLS_Write(ctx, data, dataLen, &writeLen);
    HITLS_Read(ctx, buffer, bufferLen, &readLen);
    HITLS_Close(ctx);

Sources:
[testcode/demo/client.c82-148](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L82-L148)

## Server Implementation

The server-side implementation accepts connections and handles:

    
    
    Server TLS Implementation
    
    Initialize TLS Library
    
    Create and Configure TLS Context
    
    Load Certificate and Private Key
    
    Set Up I/O
    
    Accept TLS Connection
    
    Exchange Application Data
    
    Close TLS Connection

Sources:
[testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)

Example server usage:

    
    
    // Initialize cryptographic library
    CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
    CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Configure TLS
    HITLS_Config *config = HITLS_CFG_NewTLS12Config();
    HITLS_CFG_SetClientVerifySupport(config, false);  // Optional peer verification
    HITLS_CFG_LoadCertFile(config, "server.der", TLS_PARSE_FORMAT_ASN1);
    HITLS_CFG_LoadKeyFile(config, "server.key.der", TLS_PARSE_FORMAT_ASN1);
    
    // Create TLS context
    HITLS_Ctx *ctx = HITLS_New(config);
    
    // Set up I/O
    uio = BSL_UIO_New(BSL_UIO_TcpMethod());
    BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, sizeof(fd), &infd);
    HITLS_SetUio(ctx, uio);
    
    // Accept connection, exchange data, and close
    HITLS_Accept(ctx);
    HITLS_Read(ctx, buffer, bufferLen, &readLen);
    HITLS_Write(ctx, data, dataLen, &writeLen);
    HITLS_Close(ctx);

Sources:
[testcode/demo/server.c94-173](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L94-L173)

## Error Handling

The TLS Protocol Implementation provides comprehensive error handling:

    
    
    Error Handling
    
    Error Codes
    
    Alert Messages
    
    HITLS_SUCCESS (0)
    
    HITLS_WANT_READ (3)
    
    HITLS_WANT_WRITE (4)
    
    HITLS_ERR_TLS (5)
    
    HITLS_ERR_SYSCALL (6)

Sources:
[include/tls/hitls_error.h33-73](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L33-L73)

Error categories include:

  * **Success codes** : Operation completed successfully
  * **Non-blocking I/O codes** : Operation needs more data or buffer space
  * **Protocol errors** : Violations of the TLS protocol
  * **Crypto errors** : Failures in cryptographic operations
  * **System errors** : Underlying I/O or resource issues

## Cryptographic Foundation

The TLS Protocol relies on the Cryptographic Services Layer for security
operations:

    
    
    TLS Protocol
    
    Cryptographic Services Layer
    
    Provider Framework
    
    Default Provider
    
    Custom Providers
    
    Symmetric Encryption (AES, ChaCha20)
    
    Public Key Operations (RSA, ECDSA)
    
    Hash Functions (SHA-2, SHA-3)
    
    Random Number Generation (DRBG)

Sources:
[crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
[crypto/provider/src/default/crypt_default_provider.c38-137](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L38-L137)

The TLS implementation uses this foundation for:

  * **Random Number Generation** : For nonces and key material generation
  * **Key Exchange** : For establishing shared secrets
  * **Authentication** : For verifying peer identity
  * **Bulk Encryption** : For protecting application data
  * **Message Authentication** : For ensuring data integrity

## Conclusion

The TLS Protocol Implementation in openHiTLS provides a standards-compliant,
feature-rich framework for secure communication. By supporting multiple
protocol versions, cipher suites, and extensions, it enables secure
connections across a wide range of deployment scenarios.

The modular design with clear separation between protocol layers and
cryptographic services allows for flexibility in configuration while
maintaining security. The implementation is suitable for both client and
server applications requiring secure communications.

Sources:
[config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
[include/tls/hitls_config.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h)
[tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)

# Handshake Protocol

Relevant source files

  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [crypto/curve25519/src/curve25519.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/curve25519/src/curve25519.c)
  * [crypto/dh/src/dh_core.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/dh/src/dh_core.c)
  * [crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
  * [crypto/ecc/src/ecc_pkey.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecc_pkey.c)
  * [crypto/ecc/src/ecp_mont.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ecc/src/ecp_mont.c)
  * [crypto/hybridkem/src/crypt_hybridkem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c)
  * [crypto/hybridkem/src/crypt_hybridkem_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem_local.h)
  * [crypto/mldsa/src/ml_dsa.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/mldsa/src/ml_dsa.c)
  * [crypto/provider/src/default/crypt_default_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c)
  * [include/crypto/crypt_params_key.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_params_key.h)
  * [include/tls/hitls_crypt_type.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_crypt_type.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/demo/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt)
  * [testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
  * [testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c)
  * [testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)
  * [testcode/demo/privpass_token.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c)
  * [testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
  * [testcode/demo/sm2enc.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c)
  * [testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c)
  * [testcode/testdata/provider/provider_get_cap_test1.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/testdata/provider/provider_get_cap_test1.c)
  * [tls/config/src/config_group.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c)
  * [tls/crypt/crypt_adapt/crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_adapt/crypt.c)
  * [tls/crypt/crypt_self/hitls_crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_self/hitls_crypt.c)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_ctx.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_ctx.h)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/common/src/hs_kx.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
  * [tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)
  * [tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)

The TLS Handshake Protocol in openHiTLS establishes secure connections between
clients and servers. It negotiates protocol versions, cipher suites, and
cryptographic parameters to establish shared secret keys for encrypted
communications. The handshake process is the first step in a TLS connection,
occurring before any application data can be transmitted securely.

For information about how encrypted data is transmitted after the handshake,
see the [Record Protocol](/openHiTLS/openHiTLS/4.2-record-protocol). For
details on TLS extensions configuration, see [Extensions and
Configuration](/openHiTLS/openHiTLS/4.3-extensions-and-configuration).

## Handshake Message Flow

The handshake process differs depending on the TLS version:

### TLS 1.2 Handshake Flow

    
    
    ServerClientServerClient"Secure Communication Established""ClientHello (versions, cipher suites, random)""ServerHello (selected version, cipher suite, random)""Certificate (server certificate)""ServerKeyExchange (for DHE/ECDHE)""CertificateRequest (optional)""ServerHelloDone""Certificate (if requested)""ClientKeyExchange (key exchange material)""CertificateVerify (if certificate provided)""ChangeCipherSpec""Finished (verify handshake)""ChangeCipherSpec""Finished (verify handshake)"

Sources:
[testcode/demo/client.c134-139](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L134-L139)
[testcode/demo/server.c149-154](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L149-L154)
[tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)

### TLS 1.3 Handshake Flow

    
    
    ServerClientServerClient"Key Calculation - Handshake Keys""Server Application Keys Active""Client Application Keys Active""Secure Communication Established""ClientHello (with KeyShare, SignatureAlgorithms)""ServerHello (with KeyShare)""EncryptedExtensions""Certificate (optional)""CertificateVerify (if certificate provided)""Finished""Certificate (if requested)""CertificateVerify (if certificate provided)""Finished"

In TLS 1.3, a HelloRetryRequest flow may occur if the server needs the client
to use different parameters:

    
    
    ServerClientServerClient"Continue with normal handshake...""ClientHello (with KeyShare)""HelloRetryRequest""ClientHello (with updated KeyShare)"

Sources:
[tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)
[tls/handshake/pack/src/pack_extensions.c89-118](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L89-L118)
[tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)

## Key Exchange Mechanisms

The openHiTLS library supports multiple key exchange algorithms to establish
shared secrets:

    
    
    Key Exchange Mechanisms
    
    Diffie-Hellman (DH/DHE)
    
    Elliptic Curve (ECDH/ECDHE)
    
    RSA Key Transport
    
    Pre-Shared Key (PSK)
    
    Hybrid (Post-Quantum)
    
    Supported Curves
    
    NIST P-256
    
    NIST P-384
    
    NIST P-521
    
    X25519
    
    Classical Component
    
    Post-Quantum Component
    
    ECDH
    
    X25519
    
    ML-KEM (Kyber)

Sources:
[tls/handshake/common/src/hs_kx.c38-99](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L38-L99)
[crypto/hybridkem/src/crypt_hybridkem.c39-61](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c#L39-L61)
[crypto/curve25519/src/curve25519.c31-89](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/curve25519/src/curve25519.c#L31-L89)

### Key Exchange Context

The handshake protocol manages key exchange through the `KeyExchCtx`
structure:

    
    
    contains
    
    contains
    
    KeyExchCtx
    
    +HITLS_KEY_EXCH_ALGO keyExchAlgo
    
    +void* key
    
    +uint8_t* peerPubkey
    
    +uint32_t pubKeyLen
    
    +union keyExchParam
    
    TLS_Ctx
    
    +HandshakeCtx* hsCtx
    
    +NegotiatedInfo negotiatedInfo
    
    +TLS_Config config
    
    HandshakeCtx
    
    +KeyExchCtx* kxCtx
    
    +HS_STATE state
    
    +ExtensionFlag extFlag

Sources:
[tls/handshake/common/src/hs_kx.c38-99](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L38-L99)
[tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)

### Client-Side Key Exchange Processing

For client-side ECDHE key exchange, the client processes the server's key
exchange parameters:

    
    
    HS_ProcessServerKxMsgEcdhe
    
    Extract curve type and group
    
    Verify client supports curve
    
    Save peer public key
    
    Generate ECDH key pair
    
    Store in context

Similarly, for DHE key exchange:

    
    
    HS_ProcessServerKxMsgDhe
    
    Extract DH parameters (p, g)
    
    Generate DH key pair
    
    Save peer public key
    
    Store in context

Sources:
[tls/handshake/common/src/hs_kx.c102-170](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L102-L170)
[tls/handshake/common/src/hs_kx.c172-201](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L172-L201)

### Server-Side Key Exchange Processing

For server-side ECDHE processing:

    
    
    HS_ProcessClientKxMsgEcdhe
    
    Extract client public key
    
    Store in context
    
    Use for shared secret derivation

Sources:
[tls/handshake/common/src/hs_kx.c204-236](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c#L204-L236)

## TLS Extensions

TLS extensions enhance the handshake protocol with additional functionality:

    
    
    TLS Extensions
    
    Server Name Indication
    
    Application Layer Protocol Negotiation
    
    Signature Algorithms
    
    Key Share (TLS 1.3)
    
    Pre-Shared Key
    
    Extended Master Secret
    
    Supported Groups
    
    EC Point Formats
    
    Cookie (TLS 1.3)

Extensions are packed into handshake messages using the `PackExtensionHeader`
function and extension-specific packing functions:

    
    
    Extension Packing
    
    PackExtensionHeader
    
    Extension-specific packers
    
    PackPointFormats
    
    PackSupportedGroups
    
    PackSignatureAlgorithms
    
    PackServerName
    
    PackKeyShare
    
    PackCookie

Sources:
[tls/handshake/pack/src/pack_extensions.c52-68](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L52-L68)
[tls/handshake/pack/src/pack_extensions.c89-118](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L89-L118)
[tls/handshake/pack/src/pack_extensions.c120-156](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L120-L156)

## Cryptographic Operations

The handshake protocol relies on various cryptographic operations implemented
through the cryptographic services layer:

    
    
    Handshake Protocol
    
    Cryptographic Services Layer
    
    Provider Framework
    
    Key Exchange
    
    Signature Operations
    
    Key Derivation
    
    Transcript Hashing
    
    DH Operations
    
    ECDH Operations
    
    X25519 Operations
    
    RSA Signatures
    
    ECDSA Signatures
    
    Ed25519 Signatures
    
    HKDF Key Derivation
    
    TLS 1.2 KDF

Sources:
[crypto/dh/src/dh_core.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/dh/src/dh_core.c)
[crypto/curve25519/src/curve25519.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/curve25519/src/curve25519.c)
[crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
[crypto/hybridkem/src/crypt_hybridkem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/src/crypt_hybridkem.c)

## Random Number Generation

The handshake relies heavily on secure random number generation for creating
nonces, key material, and other cryptographic values. The `CRYPT_EAL_RandInit`
function initializes the DRBG (Deterministic Random Bit Generator) used
throughout the handshake:

    
    
    CRYPT_EAL_RandInit
    
    Initialize DRBG with algorithm ID
    
    Setup entropy source
    
    Instantiate DRBG
    
    Set as global RNG

Sources:
[crypto/eal/src/eal_rand.c549-574](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L549-L574)
[crypto/eal/src/eal_rand.c593-611](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c#L593-L611)

## API Usage Examples

### Client-side Handshake Initiation

    
    
    // Initialize cryptography
    CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
    CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Configure TLS
    HITLS_Config *config = HITLS_CFG_NewTLS12Config();
    HITLS_X509_CertParseFile(BSL_FORMAT_ASN1, "ca.der", &rootCA);
    HITLS_CFG_AddCertToStore(config, rootCA, TLS_CERT_STORE_TYPE_DEFAULT, true);
    
    // Create TLS context
    HITLS_Ctx *ctx = HITLS_New(config);
    
    // Set up I/O
    BSL_UIO *uio = BSL_UIO_New(BSL_UIO_TcpMethod());
    BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, sizeof(fd), &fd);
    HITLS_SetUio(ctx, uio);
    
    // Perform handshake
    int32_t ret = HITLS_Connect(ctx);

Sources:
[testcode/demo/client.c44-147](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L44-L147)

### Server-side Handshake Acceptance

    
    
    // Initialize cryptography
    CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
    CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Configure TLS with certificates
    HITLS_Config *config = HITLS_CFG_NewTLS12Config();
    HITLS_CFG_LoadCertFile(config, "server.der", TLS_PARSE_FORMAT_ASN1);
    HITLS_CFG_LoadKeyFile(config, "server.key.der", TLS_PARSE_FORMAT_ASN1);
    
    // Create TLS context
    HITLS_Ctx *ctx = HITLS_New(config);
    
    // Set up I/O
    BSL_UIO *uio = BSL_UIO_New(BSL_UIO_TcpMethod());
    BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, sizeof(infd), &infd);
    HITLS_SetUio(ctx, uio);
    
    // Accept connection and perform handshake
    int32_t ret = HITLS_Accept(ctx);

Sources:
[testcode/demo/server.c48-173](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L48-L173)

## Error Handling

The handshake protocol uses error codes defined in `hitls_error.h` to indicate
various failure conditions:

    
    
    Handshake Errors
    
    HITLS_MSG_HANDLE_UNEXPECTED_MESSAGE
    
    HITLS_MSG_HANDLE_UNSUPPORT_VERSION
    
    HITLS_MSG_HANDLE_STATE_ILLEGAL
    
    HITLS_MSG_HANDLE_UNSUPPORT_KX_ALG
    
    HITLS_MSG_HANDLE_UNSUPPORT_CERT
    
    HITLS_MSG_HANDLE_VERIFY_FINISHED_FAIL

The handshake protocol may also return specific state indicators:

  * `HITLS_WANT_CONNECT`: Indicates the connection is blocked on the client side
  * `HITLS_WANT_ACCEPT`: Indicates the connection is blocked on the server side
  * `HITLS_WANT_READ`: Indicates waiting for data from the peer
  * `HITLS_WANT_WRITE`: Indicates a need to send data to the peer

Sources:
[include/tls/hitls_error.h33-74](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L33-L74)
[include/tls/hitls_error.h117-173](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L117-L173)

## Summary

The openHiTLS handshake protocol implementation provides a robust foundation
for establishing secure TLS connections. It supports multiple TLS versions,
various key exchange mechanisms including post-quantum hybrids, and a
comprehensive set of extensions. The modular design allows for flexibility in
cryptographic algorithms and parameters while maintaining security and
compatibility with TLS standards.

This overview covers the fundamentals of the handshake protocol
implementation. For detailed information about specific extensions, ciphers,
and configuration options, refer to other sections of the documentation.

Sources:
[testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
[testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
[tls/handshake/common/src/hs_kx.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c)
[tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
[include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)

# Record Protocol

Relevant source files

  * [.github/workflows/cmake-single-platform.yml](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-single-platform.yml)
  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [config/macro_config/hitls_config_check.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_check.h)
  * [config/macro_config/hitls_config_layer_tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_tls.h)
  * [crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)
  * [crypto/eal/src/eal_pkey_method.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_method.c)
  * [crypto/eal/src/eal_pkey_sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_sign.c)
  * [crypto/provider/src/default/crypt_default_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c)
  * [crypto/rsa/src/rsa_keyop.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_keyop.c)
  * [include/tls/hitls_config.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h)
  * [include/tls/hitls_crypt_type.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_crypt_type.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/framework/tls/rpc/src/hitls_func.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/rpc/src/hitls_func.c)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c)
  * [testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c)
  * [tls/config/src/cipher_suite.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/cipher_suite.c)
  * [tls/config/src/config_default.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_default.c)
  * [tls/config/src/config_group.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c)
  * [tls/crypt/crypt_adapt/crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_adapt/crypt.c)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_ctx.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_ctx.h)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/common/src/hs_kx.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
  * [tls/handshake/pack/src/pack_hello_verify_request.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_hello_verify_request.c)
  * [tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)
  * [tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)
  * [tls/record/src/rec_write.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c)

The Record Protocol is the foundation of the TLS protocol suite responsible
for securely transmitting data between endpoints. It provides confidentiality
and integrity protection by encapsulating higher-level protocol messages
(Handshake, Alert, Application Data) into encrypted records before
transmission over the network.

## Overview

The Record Protocol serves as the transport layer for all TLS communications.
It takes messages from higher-level protocols, fragments them if necessary,
applies cryptographic protection, and transmits them. The protocol adapts its
behavior based on whether it's operating in stream mode (TLS) or datagram mode
(DTLS).

    
    
    Record Protocol Functions
    
    Application Data
    
    TLS Record Protocol
    
    Handshake Protocol
    
    Alert Protocol
    
    Change Cipher Spec
    
    Encrypted Records
    
    Transport Layer (TCP/UDP/SCTP)
    
    Fragmentation
    
    Encryption/MAC
    
    Record Formatting

Sources:
[tls/include/tls.h53-56](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h#L53-L56)
[tls/record/src/rec_write.c35-47](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L35-L47)

## Record Format

The TLS and DTLS record formats differ slightly to accommodate the needs of
their respective transport layers:

### TLS Record Format

    
    
    TLS Record
    
    Content Type  
    (1 byte)
    
    Protocol Version  
    (2 bytes)
    
    Length  
    (2 bytes)
    
    Encrypted Fragment  
    (variable length)

### DTLS Record Format

    
    
    DTLS Record
    
    Content Type  
    (1 byte)
    
    Protocol Version  
    (2 bytes)
    
    Epoch  
    (2 bytes)
    
    Sequence Number  
    (6 bytes)
    
    Length  
    (2 bytes)
    
    Encrypted Fragment  
    (variable length)

Sources:
[tls/record/src/rec_write.c323-327](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L323-L327)
[tls/record/src/rec_write.c130-137](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L130-L137)

## Record Protocol Components

The Record Protocol implementation in openHiTLS consists of several key
components:

    
    
    contains
    
    contains
    
    contains
    
    1
    
    1
    
    1
    
    1
    
    2
    
    1
    
    RecCtx
    
    -RecBuf* outBuf
    
    -RecStates writeStates
    
    -RecStates readStates
    
    RecConnState
    
    +CipherSuiteInfo* suiteInfo
    
    +uint64_t seq
    
    +uint8_t* key
    
    +uint8_t* iv
    
    +uint8_t* macKey
    
    RecStates
    
    +RecConnState* pendingState
    
    +RecConnState* currentState
    
    RecBuf
    
    +uint8_t* buf
    
    +uint32_t start
    
    +uint32_t end
    
    +uint32_t bufSize

Sources:
[tls/record/src/rec_write.c37-47](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L37-L47)
[tls/record/src/rec_write.c141-151](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L141-L151)

## Write Operation

The Record Protocol's write operation takes plaintext data and transforms it
into secure records. The process differs between TLS (stream-based) and DTLS
(datagram-based) protocols.

    
    
    Stream (TLS)
    
    Datagram (DTLS)
    
    Yes
    
    No
    
    Application calls  
    HITLS_Write
    
    Stream or  
    Datagram?
    
    TlsRecordWrite
    
    DtlsRecordWrite
    
    TlsPlainMsgGenerate
    
    DtlsPlainMsgGenerate
    
    RecConnEncrypt
    
    Format Record Header
    
    Write Record to Network
    
    Send  
    Complete?
    
    Update Sequence Number
    
    Return WANT_WRITE

Sources:
[tls/record/src/rec_write.c247-330](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L247-L330)
[tls/record/src/rec_write.c181-245](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L181-L245)

### TLS Record Writing

For TLS, the `TlsRecordWrite` function handles writing records to the stream-
based transport. It performs the following steps:

  1. Generates a plain message structure with metadata
  2. Calculates the size of the ciphertext after encryption
  3. Encrypts the plaintext into the output buffer
  4. Formats the record header
  5. Writes the record to the transport layer
  6. Updates the sequence number

Sources:
[tls/record/src/rec_write.c247-459](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L247-L459)

### DTLS Record Writing

For DTLS, the `DtlsRecordWrite` function follows a similar process but
includes additional fields in the record header to handle packet loss and
reordering:

  1. Generates a plain message with epoch and sequence number
  2. Calculates ciphertext length
  3. Formats the DTLS record header with epoch and sequence information
  4. Encrypts the plaintext
  5. Sends the record via datagram transport
  6. Updates the sequence number

Sources:
[tls/record/src/rec_write.c181-245](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L181-L245)

## Encryption Process

The Record Protocol uses cryptographic services provided by the Cryptographic
Services Layer through the EAL (Ecosystem Abstraction Layer) interface.

    
    
    "Cryptographic Services Layer""Crypto Functions""RecConnState""Record Protocol""Cryptographic Services Layer""Crypto Functions""RecConnState""Record Protocol"GetWriteConnState()CheckEncryptionLimits()RecGetCryptoFuncs()calCiphertextLen()RecConnEncrypt()SAL_CRYPT_XXX operationsEncrypted dataRecord payloadFormat record header

The encryption process varies based on the cipher suite type:

  1. For AEAD ciphers (GCM, CCM, ChaCha20-Poly1305), a single operation provides both encryption and authentication
  2. For CBC ciphers with separate MAC algorithms, encryption and MAC are applied separately

The Record Protocol supports different encryption algorithms including:

  * AES-GCM
  * AES-CBC
  * ChaCha20-Poly1305
  * SM4-CBC/GCM (Chinese cryptographic standard)

Sources:
[crypto/provider/src/default/crypt_default_provider.c158-191](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L158-L191)
[tls/record/src/rec_write.c230-231](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L230-L231)

## Sequence Number Management

Sequence numbers are critical for the Record Protocol's security, as they:

  1. Prevent replay attacks
  2. Provide uniqueness for nonces in AEAD ciphers
  3. Enable the receiver to detect missing or reordered packets (especially in DTLS)

    
    
    Yes (>2^64-1)
    
    No
    
    Yes (>2^48-1)
    
    No
    
    TLS Seq Number  
    (64-bit counter)
    
    Overflow?
    
    Error: HITLS_REC_ERR_SN_WRAPPING
    
    Use as nonce input for encryption
    
    DTLS Seq Number  
    (48-bit) + Epoch (16-bit)
    
    Overflow?
    
    Error: HITLS_REC_ERR_SN_WRAPPING
    
    Use as nonce input for encryption

For AES-GCM specifically, there's an additional check to prevent exceeding the
algorithm's security bounds:

    
    
    if (RecConnGetSeqNum(state) > REC_MAX_AES_GCM_ENCRYPTION_LIMIT) {
        BSL_ERR_PUSH_ERROR(HITLS_REC_ENCRYPTED_NUMBER_OVERFLOW);
        // ...
    }
    

Sources:
[tls/record/src/rec_write.c53-68](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L53-L68)
[tls/record/src/rec_write.c187-192](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L187-L192)

## Transport Layer Interaction

The Record Protocol interacts with different transport layers through a
unified I/O abstraction layer:

    
    
    UIO Layer
    
    Record Protocol
    
    BSL_UIO Interface
    
    TCP Transport  
    (Stream Mode)
    
    UDP Transport  
    (Datagram Mode)
    
    SCTP Transport  
    (Stream/Datagram)
    
    BSL_UIO_Write
    
    BSL_UIO_Read
    
    BSL_UIO_Ctrl

The Record Protocol uses different write methods depending on the transport:

  1. For stream-based transports (TLS), it uses `StreamWrite` which may need to make multiple calls to send all data
  2. For datagram-based transports (DTLS), it uses `DatagramWrite` which sends the entire record in one operation

Sources:
[tls/record/src/rec_write.c247-330](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L247-L330)
[tls/record/src/rec_write.c73-104](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L73-L104)

## Error Handling

The Record Protocol defines several error codes to handle various failure
conditions:

Error Code| Description| Common Causes  
---|---|---  
`HITLS_WANT_READ`| Buffer empty, need more data| Non-blocking I/O  
`HITLS_WANT_WRITE`| Buffer full, try again later| Non-blocking I/O  
`HITLS_REC_ERR_BUFFER_NOT_ENOUGH`| Insufficient buffer size| Data too large  
`HITLS_REC_ERR_TOO_BIG_LENGTH`| Data exceeds max record size| Application
wrote too much data  
`HITLS_REC_ERR_ENCRYPT`| Encryption failed| Cryptographic error  
`HITLS_REC_ERR_SN_WRAPPING`| Sequence number overflow| Long-lived connection  
`HITLS_REC_ENCRYPTED_NUMBER_OVERFLOW`| AES-GCM encryption limit reached| Too
many records with same key  
`HITLS_REC_ERR_IO_EXCEPTION`| I/O error| Network failure  
  
Sources:
[include/tls/hitls_error.h223-249](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L223-L249)

## Integration with Higher-Level Protocols

The Record Protocol is designed to work with several higher-level protocols:

    
    
    Record Protocol (RP)
    
    Encryption
    
    Formatting
    
    Transmission
    
    Application Data
    
    RP
    
    Handshake Protocol
    
    Alert Protocol
    
    Change Cipher Spec
    
    Network Layer

These protocols use different content types to identify the type of message
being sent:

    
    
    typedef enum {
        REC_TYPE_CHANGE_CIPHER_SPEC = 20,
        REC_TYPE_ALERT = 21,
        REC_TYPE_HANDSHAKE = 22,
        REC_TYPE_APP = 23,
        REC_TYPE_END = 255
    } REC_Type;

Sources:
[tls/handshake/common/include/hs_msg.h49-71](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h#L49-L71)

## Performance Considerations

The Record Protocol includes optimizations to improve performance:

  1. Buffer management to minimize memory allocations
  2. Support for hardware-accelerated cryptographic operations through the provider framework
  3. Specialized handling for different transport types
  4. Maximum fragment length negotiation to optimize for different network conditions

Sources:
[crypto/provider/src/default/crypt_default_provider.c158-191](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L158-L191)
[tls/record/src/rec_write.c141-151](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c#L141-L151)

## Conclusion

The Record Protocol is the security foundation of TLS/DTLS communications,
responsible for encrypting and transmitting all protocol messages. It adapts
to different transport mechanisms (stream vs. datagram) and supports a wide
range of cryptographic algorithms through the provider framework. The protocol
carefully manages sequence numbers to maintain security properties and handles
various error conditions to ensure robust operation.

# Extensions and Configuration

Relevant source files

  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [config/macro_config/hitls_config_check.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_check.h)
  * [config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)
  * [config/macro_config/hitls_config_layer_tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_tls.h)
  * [crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)
  * [crypto/provider/src/default/crypt_default_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c)
  * [docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md)
  * [include/crypto/crypt_eal_init.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h)
  * [include/tls/hitls_config.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h)
  * [include/tls/hitls_crypt_type.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_crypt_type.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/framework/tls/rpc/src/hitls_func.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/rpc/src/hitls_func.c)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/consistency/tls13/test_suite_tls13_consistency_rfc8446.base.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/feature/test_suite_sdv_hlt_provider.c)
  * [tls/config/src/cipher_suite.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/cipher_suite.c)
  * [tls/config/src/config_default.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_default.c)
  * [tls/config/src/config_group.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c)
  * [tls/crypt/crypt_adapt/crypt.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/crypt/crypt_adapt/crypt.c)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_ctx.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_ctx.h)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/common/src/hs_kx.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/src/hs_kx.c)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
  * [tls/handshake/pack/src/pack_hello_verify_request.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_hello_verify_request.c)
  * [tls/handshake/recv/src/recv_server_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/recv/src/recv_server_hello.c)
  * [tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)
  * [tls/record/src/rec_write.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c)

This page documents the extension mechanisms and configuration options
available in openHiTLS for customizing TLS protocol behavior. It covers both
standard TLS extensions and custom extensions support, as well as the various
configuration parameters that can be set to control protocol versions, cipher
suites, key exchange mechanisms, and other TLS behaviors.

## 1\. TLS Extensions Overview

TLS extensions provide a mechanism to add functionality to the TLS protocol
without changing the core protocol definition. Extensions are included in the
ClientHello and ServerHello messages, allowing clients and servers to
negotiate additional capabilities.

    
    
    Extensions Types
    
    ClientHello
    
    Extensions
    
    ServerHello
    
    ServerName (SNI)
    
    SignatureAlgorithms
    
    SupportedGroups
    
    PointFormats
    
    ALPN
    
    SessionTicket
    
    RenegotiationInfo
    
    SupportedVersions
    
    PSKKeyExchangeModes
    
    KeyShare
    
    Cookie
    
    CustomExtensions

Sources:
[tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
[include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
[include/tls/hitls_config.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h)

## 2\. Extension Handling Architecture

The extension handling in openHiTLS follows a modular architecture where
extensions are packed during handshake message creation and unpacked/processed
during message reception.

    
    
    Custom Extension Handling
    
    Custom Extensions
    
    HITLS_CTX_Set_custom_ext()
    
    HITLS_CTX_add_custom_ext()
    
    Extension Handlers
    
    Extension Processing System
    
    Process Extensions
    
    Parse Extension Header
    
    Process Specific Extensions
    
    Process SNI
    
    Process Signature Algorithms
    
    Process Supported Groups
    
    Process Other Extensions
    
    Extension Packing System
    
    Pack Extensions
    
    PackExtensionHeader()
    
    Pack Specific Extensions
    
    PackServerName()
    
    PackClientSignatureAlgorithms()
    
    PackClientSupportedGroups()
    
    Other Extension Pack Functions

Sources:
[tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
[tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)

## 3\. Standard TLS Extensions

openHiTLS supports a comprehensive set of standard TLS extensions:

Extension Name| Type ID| Purpose| Availability  
---|---|---|---  
Server Name Indication (SNI)| 0| Allows client to specify target hostname| All
TLS versions  
Signature Algorithms| 13| Specifies supported signature algorithms| TLS 1.2+  
Supported Groups| 10| Specifies supported named groups for key exchange| All
TLS versions  
EC Point Formats| 11| Specifies supported point formats for elliptic curves|
All TLS versions  
ALPN| 16| Application-Layer Protocol Negotiation| All TLS versions  
Session Ticket| 35| Enables stateless session resumption| All TLS versions  
Renegotiation Info| 65281| Secure renegotiation support| All TLS versions  
Supported Versions| 43| Advertises supported TLS versions| TLS 1.3  
PSK Key Exchange Modes| 45| Indicates PSK key exchange modes| TLS 1.3  
Key Share| 51| Contains key exchange information| TLS 1.3  
Cookie| 44| Used for DoS mitigation| TLS 1.3  
Pre-Shared Key| 41| Indicates identity and PSK to use| TLS 1.3  
  
Sources:
[tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
[tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)

### 3.1 Extension Packing Logic

Extensions are packed into handshake messages using a series of specialized
functions. Each extension has conditions under which it will be included in
the message.

    
    
    Extension Need Check Functions
    
    Extension Inclusion Logic
    
    Yes
    
    No
    
    More Extensions
    
    Done
    
    Create Handshake Message
    
    Check if Extension Needed
    
    Pack Extension
    
    Skip Extension
    
    Next Extension
    
    Send Message
    
    IsNeedClientPackServerName()
    
    IsNeedPackEcExtension()
    
    IsNeedPreSharedKey()
    
    Verify Cookie Need

Sources:
[tls/handshake/pack/src/pack_extensions.c251-270](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L251-L270)
[tls/handshake/pack/src/pack_extensions.c489-515](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L489-L515)
[tls/handshake/pack/src/pack_extensions.c65-77](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c#L65-L77)

## 4\. Custom Extensions

openHiTLS provides a flexible mechanism for applications to add custom TLS
extensions.

### 4.1 Custom Extension API

The custom extension API consists of several functions to register and handle
custom extensions:

    
    
    Creates
    
    Contains
    
    CustomExtAPI
    
    +HITLS_CTX_add_custom_ext()
    
    +HITLS_CTX_Set_custom_ext()
    
    +HITLS_CUSTOM_EXT_add()
    
    CustomExtCallbacks
    
    +add_cb
    
    +parse_cb
    
    +free_cb
    
    CustomExt
    
    +ext_type
    
    +context
    
    +callbacks

Sources:
[include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
[tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)

### 4.2 Custom Extension Callbacks

When registering a custom extension, you need to provide several callback
functions:

  1. **Add Callback** : Called when constructing a ClientHello/ServerHello to add the extension data
  2. **Parse Callback** : Called when receiving an extension to parse and process the extension data
  3. **Free Callback** : Called to free any allocated resources

Example of registering a custom extension:

    
    
    // Callback functions
    int add_callback(HITLS_Ctx *ctx, unsigned int ext_type,
                     const unsigned char **out, size_t *outlen, void *add_arg);
                     
    int parse_callback(HITLS_Ctx *ctx, unsigned int ext_type,
                       const unsigned char *in, size_t inlen, void *parse_arg);
                       
    void free_callback(void *arg);
    
    // Register the extension
    HITLS_CTX_add_custom_ext(ctx, ext_type, 
                            add_callback, add_arg, free_callback,
                            parse_callback, parse_arg);

Sources:
[include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
[tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)

## 5\. Configuration Options

openHiTLS provides extensive configuration options to customize TLS behavior.

### 5.1 Protocol Versions

The library supports configuring minimum and maximum protocol versions:

    
    
    Protocol Versions
    
    Set to
    
    Set to
    
    HITLS_VERSION_TLCP_DTLCP11 (0x0101)
    
    HITLS_VERSION_SSL30 (0x0300)
    
    HITLS_VERSION_TLS10 (0x0301)
    
    HITLS_VERSION_TLS11 (0x0302)
    
    HITLS_VERSION_TLS12 (0x0303)
    
    HITLS_VERSION_TLS13 (0x0304)
    
    HITLS_VERSION_DTLS12 (0xfefd)
    
    TLS Configuration
    
    config.minVersion
    
    config.maxVersion

Sources:
[include/tls/hitls_config.h39-93](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h#L39-L93)

### 5.2 Cipher Suites

Cipher suites determine the cryptographic algorithms used for securing the
connection:

Category| Example Cipher Suites| Configuration  
---|---|---  
TLS 1.2| HITLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384| config.cipherSuites  
TLS 1.2| HITLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256| config.cipherSuites  
TLS 1.3| HITLS_AES_128_GCM_SHA256| config.cipherSuites  
TLS 1.3| HITLS_CHACHA20_POLY1305_SHA256| config.cipherSuites  
TLCP| HITLS_ECDHE_SM4_CBC_SM3| config.cipherSuites  
  
Sources:
[include/tls/hitls_config.h111-204](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h#L111-L204)
[tls/config/src/cipher_suite.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/cipher_suite.c)

The library provides a comprehensive list of supported cipher suites as
defined in
[tls/config/src/cipher_suite.c55-581](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/cipher_suite.c#L55-L581)
allowing applications to select the appropriate ciphers based on their
security and performance requirements.

### 5.3 Key Exchange Groups

Key exchange groups are used for key agreement protocols like ECDHE and DHE:

    
    
    Named Groups
    
    HITLS_EC_GROUP_CURVE25519
    
    HITLS_EC_GROUP_SECP256R1
    
    HITLS_EC_GROUP_SECP384R1
    
    HITLS_EC_GROUP_SECP521R1
    
    HITLS_EC_GROUP_BRAINPOOLP256R1
    
    HITLS_EC_GROUP_BRAINPOOLP384R1
    
    HITLS_EC_GROUP_BRAINPOOLP512R1
    
    HITLS_EC_GROUP_SM2
    
    HITLS_FF_DHE_2048
    
    HITLS_FF_DHE_3072
    
    HITLS_FF_DHE_4096
    
    HITLS_HYBRID_X25519_MLKEM768
    
    TLS Configuration
    
    config.groups

Sources:
[crypto/provider/src/default/crypt_default_provider.c261-391](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L261-L391)
[tls/config/src/config_group.c32-43](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c#L32-L43)

### 5.4 Signature Algorithms

Signature algorithms are used for authentication during the TLS handshake:

Signature Algorithm| Security Level| Configuration  
---|---|---  
RSA-PSS-RSAE-SHA256| Medium| config.signAlgorithms  
ECDSA-SECP256R1-SHA256| High| config.signAlgorithms  
ED25519| High| config.signAlgorithms  
RSA-PKCS1-SHA256| Medium| config.signAlgorithms  
SM2-SM3| National Standard (China)| config.signAlgorithms  
  
Sources:
[tls/config/src/config_group.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_group.c)

### 5.5 Extension Configuration

Various extensions can be enabled or disabled through the configuration:

    
    
    Extension Configuration
    
    config.serverName
    
    Server Name Indication
    
    config.pointFormats
    
    EC Point Formats
    
    config.alpnList
    
    ALPN Extension
    
    config.isSecureRenegotation
    
    Renegotiation Info
    
    config.isSessionResumption
    
    Session Ticket
    
    config.isSupportExtendMasterSecret
    
    Extended Master Secret

Sources:
[tls/handshake/pack/src/pack_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_extensions.c)
[tls/handshake/send/src/send_client_hello.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/send/src/send_client_hello.c)

## 6\. Feature Configuration

The openHiTLS project uses a feature-based configuration system that allows
enabling or disabling specific capabilities at build time. The feature
configuration is defined in `feature.json` and processed by the build system.

    
    
    TLS Features
    
    TLS Library Features
    
    Protocol Versions
    
    proto_tls12
    
    proto_tls13
    
    proto_tlcp11
    
    proto_dtls12
    
    Host Type
    
    host_client
    
    host_server
    
    Feature Extensions
    
    feature_renegotiation
    
    feature_alpn
    
    feature_sni
    
    feature_pha
    
    feature_psk
    
    feature_security
    
    feature_session
    
    feature_key_update
    
    feature_cert_mode
    
    feature_kem
    
    feature_custom_extensions
    
    Feature Configuration System
    
    feature.json
    
    Configure.py
    
    CMake Build Process
    
    Macro Configuration Headers
    
    Library Codebase

Sources:
[config/json/feature.json222-267](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L222-L267)
[config/json/feature.json248-267](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L248-L267)
[config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)

## 7\. Provider Framework for Cryptographic Services

OpenHiTLS includes a provider framework that allows for pluggable
cryptographic implementations through a well-defined API. This framework is
particularly important for extension mechanisms and configuration flexibility.

    
    
    Default Provider Algorithms
    
    Application
    
    TLS Layer
    
    Cryptographic Services Layer
    
    Provider Framework
    
    Default Provider
    
    Custom Providers
    
    Hash Algorithms
    
    MAC Algorithms
    
    Key Derivation Functions
    
    Symmetric Ciphers
    
    Key Management
    
    Random Number Generation
    
    Key Encapsulation Mechanisms

Sources:
[crypto/provider/src/default/crypt_default_provider.c40-196](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_provider.c#L40-L196)
[crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)

## 8\. Practical Usage Examples

### 8.1 Configuring Basic TLS Parameters

    
    
    HITLS_CFG_TLS13 *cfg = HITLS_CFG_TLS13_new();
    
    // Set protocol versions
    HITLS_CFG_SetMinProtocolVersion(cfg, HITLS_VERSION_TLS12);
    HITLS_CFG_SetMaxProtocolVersion(cfg, HITLS_VERSION_TLS13);
    
    // Set cipher suites
    uint16_t cipherSuites[] = {
        HITLS_AES_256_GCM_SHA384,
        HITLS_CHACHA20_POLY1305_SHA256,
        HITLS_AES_128_GCM_SHA256
    };
    HITLS_CFG_SetCipherSuites(cfg, cipherSuites, 3);
    
    // Set key exchange groups
    uint16_t groups[] = {
        HITLS_EC_GROUP_CURVE25519,
        HITLS_EC_GROUP_SECP256R1
    };
    HITLS_CFG_SetGroups(cfg, groups, 2);
    
    // Set Server Name Indication (SNI)
    HITLS_CFG_SetServerName(cfg, "example.com");

### 8.2 Adding a Custom Extension

    
    
    // Custom extension callback functions
    int custom_ext_add_cb(HITLS_Ctx *ctx, unsigned int ext_type,
                         const unsigned char **out, size_t *outlen, void *arg) {
        *out = my_data;
        *outlen = my_data_len;
        return 1;
    }
    
    int custom_ext_parse_cb(HITLS_Ctx *ctx, unsigned int ext_type,
                           const unsigned char *in, size_t inlen, void *arg) {
        // Process received extension data
        return 1;
    }
    
    void custom_ext_free_cb(void *arg) {
        // Free resources
    }
    
    // Register custom extension
    HITLS_CTX_add_custom_ext(ctx, MY_CUSTOM_EXT_TYPE,
                            custom_ext_add_cb, my_add_arg, custom_ext_free_cb,
                            custom_ext_parse_cb, my_parse_arg);

Sources:
[include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
[tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)

## Conclusion

The extension and configuration systems in openHiTLS provide a flexible
framework for customizing TLS behavior to meet various security and
performance requirements. By leveraging these capabilities, applications can
adapt the TLS protocol to their specific needs while maintaining conformance
with the relevant standards.

For information about building and configuration options, see [Building and
Configuration](/openHiTLS/openHiTLS/5-building-and-configuration).

# Building and Configuration

Relevant source files

  * [.github/workflows/cmake-single-platform.yml](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-single-platform.yml)
  * [CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/CMakeLists.txt)
  * [README-zh.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README-zh.md)
  * [README.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md)
  * [bsl/log/src/log.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/log/src/log.c)
  * [config/json/compile.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json)
  * [config/json/complete_options.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/complete_options.json)
  * [configure.py](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py)
  * [crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)
  * [crypto/eal/src/eal_pkey_method.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_method.c)
  * [crypto/eal/src/eal_pkey_sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_sign.c)
  * [crypto/ealinit/src/asmcap_alg_asm.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_alg_asm.c)
  * [crypto/ealinit/src/asmcap_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h)
  * [crypto/ealinit/src/crypt_init.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c)
  * [crypto/include/crypt_arm.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_arm.h)
  * [crypto/rsa/src/rsa_keyop.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_keyop.c)
  * [crypto/sha1/src/noasm_sha1.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1.c)
  * [crypto/sha1/src/noasm_sha1_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1_small.c)
  * [crypto/sha2/src/noasm_sha256.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256.c)
  * [crypto/sha2/src/noasm_sha256_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256_small.c)
  * [crypto/sha2/src/noasm_sha512.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512.c)
  * [crypto/sha2/src/noasm_sha512_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512_small.c)
  * [crypto/sm3/src/noasm_sm3.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sm3/src/noasm_sm3.c)
  * [docs/en/4_User Guide/1_Build and Installation Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User Guide/1_Build and Installation Guide.md)
  * [include/bsl/bsl_log.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/bsl/bsl_log.h)
  * [testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c)
  * [testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c)
  * [testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c)

This page provides a comprehensive guide to building, configuring, and
integrating the openHiTLS library. It covers the build system architecture,
configuration options, assembly optimizations, and common build scenarios. For
more detailed information about specific configuration options, refer to the
corresponding subsections.

## Build System Overview

The openHiTLS build system uses a two-stage process: a Python-based
configuration stage followed by a CMake-based build stage. This architecture
allows for flexible configuration while maintaining compatibility with
standard build tools.

    
    
    Build Stage
    
    Configuration Stage
    
    Generates
    
    Read by
    
    Read by
    
    Read by
    
    Used by
    
    Generates
    
    Builds
    
    Input to
    
    configure.py
    
    modules.cmake
    
    feature.json
    
    compile.json
    
    complete_options.json
    
    CMake
    
    Makefile
    
    Libraries
    
    User Arguments

Sources:
[configure.py1-536](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L1-L536)
[.github/workflows/cmake-single-
platform.yml1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L1-L53)
[CMakeLists.txt1-26](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/CMakeLists.txt#L1-L26)

### Configuration Components

The configuration system consists of several key components:

  1. **configure.py** : The main configuration script that processes user arguments and generates build files
  2. **Configuration files** : JSON files that define available options and defaults 
     * **feature.json** : Defines available features and their dependencies
     * **compile.json** : Defines default compiler and linker options
     * **complete_options.json** : Lists all available compiler and linker options
  3. **modules.cmake** : Generated file that defines how to build each module

Sources:
[configure.py146-256](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L146-L256)
[configure.py258-444](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L258-L444)

## Build Prerequisites

Before building openHiTLS, ensure you have the following dependencies
installed:

Dependency| Minimum Version| Description  
---|---|---  
GCC| 7.3.0| C compiler  
Python| 3.5| For configuration scripts  
CMake| 3.16| Build system  
libboundscheck| -| Security library (required)  
  
### Setting Up the Build Environment

  1. **Clone the repository with dependencies:**
         
         git clone --recurse-submodules https://gitcode.com/openhitls/openhitls.git
         

  2. **Build the security library:**
         
         cd openHiTLS/platform/Secure_C
         make -j
         

Sources:
[README.md1-101](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L1-L101)
[README-
zh.md1-101](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README-
zh.md#L1-L101)

## Basic Build Process

The build process follows these steps:

  1. **Prepare the build directory:**
         
         cd openHiTLS && mkdir -p ./build && cd ./build
         

  2. **Configure the build:**
         
         python3 ../configure.py [options]
         

  3. **Generate the build system:**
         
         cmake ..
         

  4. **Build the libraries:**
         
         make
         

  5. **Install (optional):**
         
         make install
         

    
    
    MakeCMake"configure.py"UserMakeCMake"configure.py"UserParse argumentspython3 ../configure.py [options]Load configuration filesUpdate feature configurationUpdate compile configurationGenerate modules.cmakecmake ..Process CMakeLists.txtProcess modules.cmakeGenerate MakefilesmakeBuild librariesmake installInstall libraries

Sources:
[configure.py505-527](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L505-L527)
[.github/workflows/cmake-single-
platform.yml28-36](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L28-L36)
[README.md67-96](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L67-L96)

## Configuration Options

The `configure.py` script offers numerous options to customize the build. Here
are the most important ones:

### Core Configuration Options

Option| Description| Example  
---|---|---  
`--enable`| Enable specific components or features| `--enable hitls_bsl
hitls_crypto hitls_tls`  
`--disable`| Disable specific features| `--disable uio_sctp`  
`--lib_type`| Specify library type(s)| `--lib_type static shared`  
`--bits`| Specify system bits (32 or 64)| `--bits=64`  
`--system`| Specify target system| `--system=linux`  
`--endian`| Specify endianness| `--endian=little`  
  
### Compiler and Linker Options

Option| Description| Example  
---|---|---  
`--add_options`| Add compiler options| `--add_options="-O0 -g"`  
`--del_options`| Remove compiler options| `--del_options="-O2 -Werror"`  
`--add_link_flags`| Add linker flags| `--add_link_flags="-ldl"`  
`--del_link_flags`| Remove linker flags| `--del_link_flags="-shared"`  
  
### Assembly Optimization Options

Option| Description| Example  
---|---|---  
`--asm_type`| Specify assembly optimization type| `--asm_type x8664`  
`--asm`| Specify features to optimize with assembly| `--asm sm3 aes`  
  
Sources:
[configure.py86-145](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L86-L145)
[.github/workflows/cmake-single-
platform.yml31](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L31-L31)
[config/json/complete_options.json1-220](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/complete_options.json#L1-L220)

## Common Build Scenarios

### Basic Build (C Implementation)

To build all components using C implementations:

    
    
    python3 ../configure.py --enable hitls_bsl hitls_crypto hitls_tls hitls_pki hitls_auth --lib_type static --bits=64 --system=linux
    

### Optimized Build (with Assembly)

To build with assembly optimizations on x86_64:

    
    
    python3 ../configure.py --enable hitls_bsl hitls_crypto hitls_tls hitls_pki hitls_auth --lib_type static --bits=64 --system=linux --asm_type x8664
    

### Debug Build

For debugging with debug symbols and no optimization:

    
    
    python3 ../configure.py --enable hitls_bsl hitls_crypto hitls_tls --lib_type static --add_options="-O0 -g" --del_options="-O2"
    

Sources:
[README.md77-87](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L77-L87)
[.github/workflows/cmake-single-
platform.yml31](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L31-L31)

## Cryptographic Module Initialization

openHiTLS provides various cryptographic algorithms, and the build system
allows for customizing which ones are included and how they're initialized.
The initialization mechanism uses a constructor attribute to automatically
initialize components when the library is loaded.

    
    
    Initialization Flow
    
    Runtime detection
    
    Selects
    
    Cleanup Flow
    
    CRYPT_EAL_Cleanup
    
    RandModuleFree
    
    BslModuleFree
    
    ProviderModuleFree
    
    GlobalLockFree
    
    CRYPT_EAL_Init
    
    GetCpuInstrSupportState
    
    BslModuleInit
    
    RandModuleInit
    
    ProviderModuleInit
    
    GlobalLockInit
    
    CPU Features
    
    Optimal Algorithm Implementations

The initialization process can be controlled with several build options:

Option| Description| Value  
---|---|---  
`-DHITLS_EAL_INIT_OPTS`| Controls which components are auto-initialized|
Bitmap value  
`-DHITLS_CRYPTO_ASM_CHECK`| Enables runtime CPU feature detection| Flag  
`-DHITLS_CRYPTO_ENTROPY`| Enables entropy collection for random number
generation| Flag  
  
The `HITLS_EAL_INIT_OPTS` value is a bitmap:

Bit Position| Component  
---|---  
0| CPU capability detection  
1| BSL (Base Support Layer)  
2| Random number generation  
3| Provider framework  
4| Provider-based random number generation  
5| Global locks  
  
Sources:
[crypto/ealinit/src/crypt_init.c1-451](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L1-L451)
[testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c1-324](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c#L1-L324)

## Memory Optimization Options

openHiTLS provides options to optimize memory footprint for constrained
environments. The following options are available:

Option| Description| Effect  
---|---|---  
`-DHITLS_CRYPTO_SHA1_SMALL_MEM`| Use memory-optimized SHA-1| ~70% less ROM,
lower performance  
`-DHITLS_CRYPTO_SHA256_SMALL_MEM`| Use memory-optimized SHA-256| ~65% less
ROM, lower performance  
`-DHITLS_CRYPTO_SHA512_SMALL_MEM`| Use memory-optimized SHA-512| ~70% less
ROM, lower performance  
`-DHITLS_CRYPTO_AES_PRECALC_TABLES`| Use pre-calculated tables for AES| Faster
but larger code size  
  
These options allow you to balance between performance and code size based on
your requirements. For example, to build with small memory footprint:

    
    
    python3 ../configure.py --enable hitls_bsl hitls_crypto --add_options="-DHITLS_CRYPTO_SHA256_SMALL_MEM -DHITLS_CRYPTO_SHA512_SMALL_MEM"
    

Sources:
[crypto/sha1/src/noasm_sha1_small.c1-125](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1_small.c#L1-L125)
[crypto/sha2/src/noasm_sha256_small.c1-123](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256_small.c#L1-L123)
[crypto/sha2/src/noasm_sha512_small.c1-127](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512_small.c#L1-L127)

## Assembly Optimization

openHiTLS provides assembly-optimized implementations for critical
cryptographic algorithms on supported platforms. The assembly optimizations
are selected at runtime based on CPU feature detection.

    
    
    Runtime Selection
    
    AVX/NEON Available
    
    Features Not Available
    
    Enables
    
    Makes available
    
    Verifies CPU support for
    
    Application
    
    CRYPT_EAL_Init
    
    GetCpuInstrSupportState
    
    CPU Feature Detection
    
    Assembly Implementation
    
    Generic C Implementation
    
    configure.py --asm_type
    
    Assembly Code Compilation
    
    CRYPT_ASMCAP_*
    
    Algorithm Implementation

### Supported Assembly Types

The following assembly types are supported:

Assembly Type| Architecture| Description  
---|---|---  
`x8664`| x86_64| Intel/AMD 64-bit optimizations  
`armv8`| AArch64| ARMv8 NEON/AES optimizations  
  
### Enabling Assembly Optimizations

Assembly optimizations can be enabled during configuration:

    
    
    python3 ../configure.py --enable hitls_crypto --asm_type armv8 --asm sm3 aes
    

This enables ARMv8 assembly optimizations for SM3 and AES algorithms.

Sources:
[crypto/ealinit/src/asmcap_local.h1-50](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h#L1-L50)
[crypto/ealinit/src/asmcap_alg_asm.c1-50](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_alg_asm.c#L1-L50)
[configure.py225-236](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L225-L236)

## Version Information

openHiTLS provides version information that can be accessed at runtime. This
information is defined during the build process.

Function| Description  
---|---  
`BSL_LOG_GetVersion`| Returns the version string  
`BSL_LOG_GetVersionNum`| Returns the version number  
  
The version is defined in the build system and can be overridden with:

    
    
    python3 ../configure.py --hitls_version="Custom Version String" --hitls_version_num=0x12345678
    

Sources:
[include/bsl/bsl_log.h77-106](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/bsl/bsl_log.h#L77-L106)
[bsl/log/src/log.c1-100](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/log/src/log.c#L1-L100)
[testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c169-184](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c#L169-L184)

## Troubleshooting Build Issues

Common build issues and their solutions:

Issue| Solution  
---|---  
Missing dependency| Check prerequisites section and install required
dependencies  
Configuration fails| Verify command-line arguments and check for any syntax
errors  
Compilation errors| Check compiler version and ensure all dependencies are
installed  
Link errors| Check for missing libraries and ensure correct link flags are
used  
  
If you encounter "unknown CPU instruction" errors during compilation, it may
indicate that you've selected assembly optimizations for an unsupported
architecture. Try disabling assembly optimizations or selecting the
appropriate architecture.

Sources: [.github/workflows/cmake-single-
platform.yml1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L1-L53)
[configure.py505-536](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L505-L536)

## Advanced Configuration

For advanced users who need fine-grained control over the build process,
openHiTLS supports direct specification of configuration files.

    
    
    python3 ../configure.py --feature_config path/to/feature_config.json --compile_config path/to/compile_config.json
    

This allows you to bypass command-line arguments and directly specify the
configuration files.

You can also export the current configuration to JSON files for future reuse:

  1. Configure with command-line arguments
  2. The configuration is saved to `build/feature_config.json` and `build/compile_config.json`
  3. Reuse these files for future builds

Sources:
[configure.py64-67](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L64-L67)
[configure.py96-100](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L96-L100)

# Build System

Relevant source files

  * [.github/workflows/cmake-single-platform.yml](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-single-platform.yml)
  * [CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/CMakeLists.txt)
  * [README-zh.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README-zh.md)
  * [README.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md)
  * [bsl/log/src/log.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/log/src/log.c)
  * [config/json/compile.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json)
  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [configure.py](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py)
  * [crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)
  * [crypto/eal/src/eal_pkey_method.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_method.c)
  * [crypto/eal/src/eal_pkey_sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_sign.c)
  * [crypto/ealinit/src/asmcap_alg_asm.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_alg_asm.c)
  * [crypto/ealinit/src/asmcap_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h)
  * [crypto/ealinit/src/crypt_init.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c)
  * [crypto/include/crypt_arm.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_arm.h)
  * [crypto/rsa/src/rsa_keyop.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_keyop.c)
  * [docs/en/4_User Guide/1_Build and Installation Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User Guide/1_Build and Installation Guide.md)
  * [include/bsl/bsl_log.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/bsl/bsl_log.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/log/test_suite_sdv_log.c)
  * [testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c)
  * [testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)

The openHiTLS build system enables flexible configuration and compilation of
the library for different environments and use cases. This document explains
the build system architecture, configuration process, and how to customize the
build according to your needs.

For information about specific configuration options, see [Configuration
Options](/openHiTLS/openHiTLS/5.2-configuration-options). For details on
assembly optimizations, see [Assembly
Optimizations](/openHiTLS/openHiTLS/5.3-assembly-optimizations).

## Overview

The openHiTLS build system uses a combination of Python and CMake to provide a
flexible and powerful build process. The system is designed to allow fine-
grained control over which features are included in the build, which
cryptographic algorithms are supported, and how they are implemented (e.g.,
with or without assembly optimizations).

The build process follows a two-step approach:

  1. Configuration: Using a Python script to generate CMake configuration
  2. Compilation: Using CMake and the native build system to compile the code

This approach allows for greater flexibility in configuration while leveraging
the cross-platform capabilities of CMake for the actual build process.

### Build System Architecture

    
    
    Command Line Arguments
    
    Input Configuration Files
    
    configure.py
    
    Configuration Processing
    
    feature_config.json
    
    compile_config.json
    
    modules.cmake
    
    CMake Build Process
    
    Compiled Libraries
    
    Test Executables
    
    feature.json
    
    compile.json
    
    complete_options.json
    
    --enable
    
    --disable
    
    --asm_type
    
    --lib_type
    
    ...other options

Sources:
[configure.py1-536](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L1-L536)
[config/json/feature.json1-631](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L1-L631)
[config/json/compile.json1-52](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json#L1-L52)
[.github/workflows/cmake-single-
platform.yml1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L1-L53)

## Configuration Process

The configuration process is handled by `configure.py`, which parses command-
line arguments, reads configuration files, and generates the necessary CMake
files.

### Configuration Flow

    
    
    CMake Build SystemCMakeGeneratorCompileParserFeatureParserconfigure.pyUserCMake Build SystemCMakeGeneratorCompileParserFeatureParserconfigure.pyUserRun with options (--enable, --asm_type, etc.)Load feature definitions from feature.jsonLoad compile options from compile.jsonCreate feature_config.json and compile_config.jsonGenerate modules.cmakeRun CMake with generated configBuilt libraries and executables

Sources:
[configure.py146-244](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L146-L244)
[configure.py258-504](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L258-L504)

### Command-Line Options

The `configure.py` script supports numerous command-line options to customize
the build:

Option| Description| Example  
---|---|---  
`--enable`| Specify features to build| `--enable hitls_bsl hitls_crypto`  
`--disable`| Specify features to exclude| `--disable uio_sctp`  
`--asm_type`| Specify assembly architecture| `--asm_type x8664`  
`--lib_type`| Specify library types to build| `--lib_type static shared`  
`--system`| Specify target system| `--system linux`  
`--bits`| Specify system bit width| `--bits 64`  
`--add_options`| Add compiler options| `--add_options="-O0 -g"`  
`--add_link_flags`| Add linker flags| `--add_link_flags="-ldl"`  
`--build_dir`| Specify build directory| `--build_dir build`  
  
Sources:
[configure.py83-129](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L83-L129)

### Configuration Example

Here's an example of configuring a full build with static libraries and x86-64
assembly optimizations:

    
    
    python3 ../configure.py --enable hitls_bsl hitls_crypto hitls_tls hitls_pki hitls_auth --lib_type static --bits=64 --system=linux --asm_type x8664
    

Sources: [.github/workflows/cmake-single-
platform.yml28-31](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L28-L31)
[README.md83-86](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L83-L86)

## Feature Selection and Dependency Management

OpenHiTLS implements a sophisticated feature selection and dependency
resolution system. Features are organized hierarchically, with dependencies
between them defined in `feature.json`.

### Feature Structure

    
    
    Libraries (hitls_bsl, hitls_crypto, etc.)
    
    Features (c, x8664, armv8)
    
    Sub-features (md, cipher, pkey, etc.)
    
    Specific Implementations (sha256, aes, rsa, etc.)
    
    Dependencies
    
    Options

Sources:
[config/json/feature.json1-631](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L1-L631)

### Dependency Resolution

The build system automatically resolves dependencies between features. When a
feature is enabled, all of its dependencies are also enabled.

For example, enabling the `hkdf` feature will automatically enable its
dependencies (`hmac` and `params`):

    
    
    "hkdf": {
        "deps": ["hmac", "params"]
    }

Similarly, for features with options, the build system ensures that at least
one of the options is enabled:

    
    
    "hpke": {
        "deps": ["hkdf", "params"],
        "opts": [["aes", "chacha20"], ["ecc", "x25519"]]
    }

This means that for `hpke` to work, it needs either `aes` or `chacha20`, and
either `ecc` or `x25519`.

Sources:
[config/json/feature.json72-76](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L72-L76)
[configure.py146-244](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L146-L244)

## Module Generation

The build system generates modules based on the selected features and their
dependencies. Each module corresponds to a set of source files and headers
that implement a specific feature.

### Module Structure

    
    
    Library (e.g., hitls_crypto)
    
    Module (e.g., aes)
    
    Source Files
    
    Include Directories
    
    Dependencies
    
    Features (e.g., aes)
    
    Architecture (e.g., x8664)

Sources:
[config/json/feature.json632-810](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L632-L810)
[configure.py258-357](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L258-L357)

### Library Types

The build system supports generating three types of libraries:

  1. **Static Libraries** (`*.a`): Linked statically into applications
  2. **Shared Libraries** (`*.so`): Dynamically linked at runtime
  3. **Object Libraries** (`*.o`): Can be linked directly without archiving

The library type is specified with the `--lib_type` option:

    
    
    --lib_type static shared object
    

Sources:
[configure.py392-443](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L392-L443)

## Assembly Optimizations

OpenHiTLS includes assembly-optimized implementations of cryptographic
algorithms for better performance. The build system enables selecting
different assembly implementations based on the target architecture.

### Architecture Selection

The architecture is specified with the `--asm_type` option:

    
    
    --asm_type x8664
    --asm_type armv8
    

The build system then selects the appropriate assembly implementations for the
chosen architecture.

Sources:
[config/json/feature.json194-219](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L194-L219)
[configure.py106-108](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L106-L108)

### Assembly Capability Detection

At runtime, the library checks for CPU capabilities to ensure that the
selected assembly implementations are supported:

    
    
    Yes
    
    No
    
    Application Initialization
    
    CRYPT_EAL_Init
    
    GetCpuInstrSupportState
    
    Check for CPU Features
    
    Features Available?
    
    Use Optimized Implementation
    
    Fall back to Generic Implementation

Sources:
[crypto/ealinit/src/crypt_init.c175-205](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L175-L205)
[crypto/ealinit/src/asmcap_local.h1-96](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h#L1-L96)

## CMake Integration

OpenHiTLS uses CMake as its build system generator. The `configure.py` script
generates a `modules.cmake` file that defines all the targets and their
dependencies.

### CMake Structure

    
    
    modules.cmake
    
    Project Definitions
    
    Module Targets
    
    Library Targets
    
    Object Libraries
    
    Static Libraries
    
    Shared Libraries
    
    Object Files
    
    Installation Rules

Sources:
[configure.py358-444](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/configure.py#L358-L444)
[testcode/sdv/CMakeLists.txt1-234](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt#L1-L234)
[testcode/framework/tls/CMakeLists.txt1-108](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt#L1-L108)

## Test Integration

OpenHiTLS includes a comprehensive test framework that is tightly integrated
with the build system. The tests are built using the same build system as the
library itself.

### Test Build Structure

    
    
    Test Source Files
    
    Test Executables
    
    Test Libraries
    
    Main Library
    
    Test Framework
    
    Test Configuration

Sources:
[testcode/sdv/CMakeLists.txt18-234](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt#L18-L234)
[testcode/framework/tls/CMakeLists.txt14-108](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt#L14-L108)

## CI/CD Integration

OpenHiTLS includes GitHub Actions workflows for continuous integration and
delivery. These workflows use the build system to build and test the library
on various platforms.

    
    
    Test ScriptsMakeCMakeconfigure.pyGitHub ActionsTest ScriptsMakeCMakeconfigure.pyGitHub ActionsRun configure.py with optionsGenerate build filesBuild library and testsRun testsReport test results

Sources: [.github/workflows/cmake-single-
platform.yml1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L1-L53)

## Conclusion

The openHiTLS build system provides a flexible and powerful way to configure
and build the library for different environments and use cases. By using a
combination of Python and CMake, it offers both ease of configuration and
cross-platform compatibility.

The key features of the build system include:

  * Fine-grained control over which features are included
  * Support for multiple library types (static, shared, object)
  * Assembly optimizations for different architectures
  * Automatic dependency resolution
  * Integration with the test framework
  * Support for CI/CD workflows

For more information on specific configuration options, see [Configuration
Options](/openHiTLS/openHiTLS/5.2-configuration-options). For details on
assembly optimizations, see [Assembly
Optimizations](/openHiTLS/openHiTLS/5.3-assembly-optimizations).

# Configuration Options

Relevant source files

  * [README-zh.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README-zh.md)
  * [README.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md)
  * [config/json/compile.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json)
  * [config/json/complete_options.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/complete_options.json)
  * [config/json/feature.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json)
  * [config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)
  * [crypto/ealinit/src/asmcap_alg_asm.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_alg_asm.c)
  * [crypto/ealinit/src/asmcap_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h)
  * [crypto/ealinit/src/crypt_init.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c)
  * [crypto/include/crypt_arm.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_arm.h)
  * [crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)
  * [crypto/sha1/src/noasm_sha1.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1.c)
  * [crypto/sha1/src/noasm_sha1_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1_small.c)
  * [crypto/sha2/src/noasm_sha256.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256.c)
  * [crypto/sha2/src/noasm_sha256_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256_small.c)
  * [crypto/sha2/src/noasm_sha512.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512.c)
  * [crypto/sha2/src/noasm_sha512_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512_small.c)
  * [crypto/sm3/src/noasm_sm3.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sm3/src/noasm_sm3.c)
  * [docs/en/4_User Guide/1_Build and Installation Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User Guide/1_Build and Installation Guide.md)
  * [docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md)
  * [include/crypto/crypt_eal_init.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h)
  * [include/tls/hitls_custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h)
  * [include/tls/hitls_error.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h)
  * [testcode/framework/tls/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt)
  * [testcode/sdv/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt)
  * [testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.c)
  * [testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/tls/custom/test_suite_sdv_custom_extensions.data)
  * [tls/feature/custom_extensions/include/custom_extensions.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h)
  * [tls/feature/custom_extensions/src/custom_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/src/custom_extensions.c)
  * [tls/handshake/common/include/hs_msg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/common/include/hs_msg.h)
  * [tls/handshake/pack/src/pack_encrypted_extensions.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_encrypted_extensions.c)
  * [tls/include/tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h)
  * [tls/include/tls_binlog_id.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls_binlog_id.h)

This page provides a comprehensive overview of the configuration options
available in openHiTLS. It covers how to customize the library's features,
build settings, and runtime behavior to meet specific requirements for
security, performance, and functionality.

## 1\. Configuration System Overview

openHiTLS uses a flexible configuration system that allows customization at
multiple levels:

  1. **Feature Selection** \- Choose which cryptographic algorithms, protocols, and capabilities to include
  2. **Build Configuration** \- Set compiler flags, optimization levels, and architecture-specific optimizations
  3. **Runtime Configuration** \- Configure TLS parameters, cipher suites, and protocol behavior

The configuration process primarily uses the `configure.py` script which
processes user options, updates configuration files, and generates build files
for CMake.

    
    
    configure.py
    
    Parse Arguments
    
    Update Configurations
    
    Generate modules.cmake
    
    CMake Build Process
    
    feature.json
    
    compile.json
    
    complete_options.json
    
    Feature Selections
    
    Compiler Options
    
    Assembly Optimizations
    
    Compiled Libraries
    
    Test Executables

Sources:
[config/json/feature.json1-631](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L1-L631)
[config/json/compile.json1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json#L1-L53)
[config/json/complete_options.json1-221](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/complete_options.json#L1-L221)
[testcode/sdv/CMakeLists.txt1-235](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/CMakeLists.txt#L1-L235)
[testcode/framework/tls/CMakeLists.txt1-109](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/CMakeLists.txt#L1-L109)

## 2\. Feature Configuration

openHiTLS organizes functionality into multiple libraries, each with
configurable features:

  * **hitls_bsl** \- Base Support Layer
  * **hitls_crypto** \- Cryptographic algorithms
  * **hitls_tls** \- TLS protocol implementation
  * **hitls_pki** \- PKI and certificate handling
  * **hitls_auth** \- Authentication mechanisms

Each feature can have dependencies on other features, ensuring all necessary
components are included.

    
    
    Feature Example
    
    Libraries
    
    hitls_bsl
    
    hitls_crypto
    
    hitls_tls
    
    hitls_pki
    
    hitls_auth
    
    ECDSA
    
    ECC
    
    Bignum Operations
    
    SHA Hash Functions

### 2.1 Feature Definition Format

Features are defined in `feature.json` with their dependencies and options:

    
    
    "feature_name": {
        "deps": ["dependency1", "dependency2"],
        "opts": [["option1", "option2"], ["option3", "option4"]]
    }

  * **deps** \- Required dependencies that must be enabled
  * **opts** \- Optional features, where at least one from each array must be enabled

Sources:
[config/json/feature.json1-631](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L1-L631)

### 2.2 Key Feature Categories

#### 2.2.1 Cryptographic Algorithms

Category| Available Algorithms  
---|---  
Hash Functions| MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3, SM3  
Symmetric Encryption| AES (ECB, CBC, CTR, GCM, CCM, XTS), ChaCha20-Poly1305,
SM4  
Public Key| RSA, DSA, ECDSA, ECDH, SM2, Ed25519, X25519, MLKEM (post-quantum)  
MAC| HMAC, CMAC, GMAC, CBC-MAC, SipHash  
Key Derivation| HKDF, PBKDF2, SCRYPT  
Random Generation| DRBG (Hash, HMAC, CTR)  
  
Sources:
[config/json/feature.json40-205](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L40-L205)
[config/macro_config/hitls_config_layer_crypto.h1-775](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L1-L775)

#### 2.2.2 TLS Protocol Features

Feature| Description  
---|---  
Protocol Versions| TLS 1.2, TLS 1.3, DTLS 1.2, TLCP 1.1  
Host Types| Client, Server  
Extensions| SNI, ALPN, PSK, EMS, Cert Mode, Session Resume  
PHA| Post-Handshake Authentication  
Custom Extensions| User-defined TLS extensions  
  
Sources:
[config/json/feature.json222-582](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L222-L582)
[tls/feature/custom_extensions/include/custom_extensions.h1-83](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/feature/custom_extensions/include/custom_extensions.h#L1-L83)

#### 2.2.3 Cipher Suites

TLS supports numerous cipher suites which determine the security properties of
connections. The available suites are defined in the feature configuration:

    
    
    Cipher Suite
    
    Key Exchange
    
    Authentication
    
    Encryption
    
    Hash Function
    
    RSA
    
    ECDHE
    
    DHE
    
    RSA
    
    ECDSA
    
    PSK
    
    AES-GCM
    
    AES-CBC
    
    ChaCha20-Poly1305
    
    SHA256
    
    SHA384

Example suite: `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` uses ECDHE for key
exchange, RSA for authentication, AES-256-GCM for encryption, and SHA-384 for
hashing.

Sources:
[config/json/feature.json290-503](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L290-L503)

## 3\. Build Configuration

### 3.1 Compiler Options

The build system supports extensive customization of compiler flags for
different purposes:

Flag Category| Description| Examples  
---|---|---  
Language Flags| C language standard| `-std=c99`, `-std=c11`  
Warning Flags| Code quality checks| `-Wall`, `-Werror`, `-Wextra`  
Security Flags| Security enhancements| `-fstack-protector-all`, `-fPIC`  
Optimization Flags| Performance settings| `-O2`, `-Os`, `-fno-strict-aliasing`  
Debug Flags| Debugging support| `-g`, `-g3`  
Architecture Flags| CPU-specific options| `-march=armv8-a`,
`-mtune=cortex-a57`  
  
Sources:
[config/json/complete_options.json2-202](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/complete_options.json#L2-L202)
[config/json/compile.json2-41](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json#L2-L41)

### 3.2 Assembly Optimizations

The library supports assembly-optimized implementations for improved
performance on specific architectures:

    
    
    Optimized Algorithms
    
    Assembly Optimizations
    
    Architecture Selection
    
    x86_64
    
    ARMv8
    
    AES-NI
    
    AVX/AVX2/AVX512
    
    BMI1/BMI2
    
    NEON
    
    AES/SHA Extensions
    
    AES
    
    SHA1/SHA2
    
    ChaCha20-Poly1305
    
    ECC Operations

Assembly optimizations are controlled through `feature.json` and are
architecture-specific:

    
    
    "x8664": {
        "sha1": {"ins_set":["x8664", "avx512"]},
        "sha2": {"ins_set":["x8664", "avx512"]},
        "aes": {"ins_set":["x8664", "avx512"]},
        "chacha20": {"ins_set":["x8664", "avx512"]}
    }

Sources:
[config/json/feature.json194-219](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L194-L219)
[crypto/ealinit/src/asmcap_alg_asm.c1-7001](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_alg_asm.c#L1-L7001)
[crypto/ealinit/src/crypt_init.c1-759](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L1-L759)

### 3.3 Configuration Command Line

The build is configured using the `configure.py` script with various options:

    
    
    python3 configure.py --enable [libraries] --lib_type [static/shared] --bits [32/64] --system [os] --asm_type [arch]

Examples:

  * Full build with all libraries: `--enable hitls_bsl hitls_crypto hitls_tls hitls_pki hitls_auth`
  * x86-64 optimized build: `--asm_type x8664`
  * Static library build: `--lib_type static`

Sources:
[README.md67-86](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L67-L86)
[README-
zh.md67-86](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README-
zh.md#L67-L86)

## 4\. Runtime Configuration

Runtime configuration controls the behavior of the library during operation.

### 4.1 TLS Context Configuration

The TLS context is configured using the `HITLS_CtxConfig` structure:

    
    
    typedef struct TLSCtxConfig {
        void *userData;                         /* user data */
        uint16_t pmtu;                          /* Maximum transport unit of a path (bytes) */
        bool isSupportPto;                      /* is support process based TLS offload */
        TLS_Config tlsConfig;                   /* tls configure context */
    } TLS_CtxConfig;

Key configuration options include:

  * Protocol versions
  * Cipher suites
  * Certificate settings
  * Key exchange algorithms
  * Custom extensions

Sources:
[tls/include/tls.h186-194](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/include/tls.h#L186-L194)
[include/tls/hitls_custom_extensions.h1-266](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_custom_extensions.h#L1-L266)

### 4.2 Error Handling Configuration

Error handling is a critical aspect of configuration, providing detailed
diagnostic information:

    
    
    Error Occurs
    
    Error Code Generated
    
    Error Stack Recorded
    
    Application Retrieves Error
    
    HITLS_GetError()
    
    BSL_ERR_GetLastErrorFileLine()
    
    File/Line Information
    
    Error Handling by Application

Error codes are organized by module, with specific ranges for different
components:

Module| Error Code Range  
---|---  
General| 0x02010001-0x0201FFFF  
Configuration| 0x02020001-0x0202FFFF  
Connection| 0x02030001-0x0203FFFF  
Handshake| 0x02040001-0x0204FFFF  
Record| 0x020A0001-0x020AFFFF  
Certificate| 0x020C0001-0x020CFFFF  
Cryptographic| 0x020D0001-0x020DFFFF  
  
Sources:
[include/tls/hitls_error.h81-415](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L81-L415)

### 4.3 Initialization Configuration

The library can be automatically initialized with constructor attributes or
manually initialized. The initialization process sets up:

  * CPU capability detection
  * Basic Support Layer (BSL)
  * Random number generation
  * Provider framework

This can be controlled with the following macros:

  * `HITLS_EAL_INIT_OPTS` \- Controls initialization options
  * `HITLS_CRYPTO_INIT_RAND_ALG` \- Sets the random algorithm to use

Sources:
[crypto/ealinit/src/crypt_init.c176-244](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L176-L244)
[testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c1-323](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c#L1-L323)

## 5\. Example Configurations

### 5.1 Minimal TLS Client

    
    
    {
      "enable": ["hitls_bsl", "hitls_crypto", "hitls_tls"],
      "features": {
        "hitls_bsl": ["err", "sal", "log"],
        "hitls_crypto": [
          "sha256", "aes", "rsa", "ecdsa", "ecdh",
          "hmac", "hkdf", "drbg"
        ],
        "hitls_tls": [
          "proto_tls12", "host_client", 
          "suite_aes_128_gcm_sha256",
          "suite_ecdhe_rsa_with_aes_128_gcm_sha256"
        ]
      },
      "compile": {
        "optimization": "-Os",
        "security": ["-fPIC", "-fstack-protector"]
      }
    }

### 5.2 High-Security Server

    
    
    {
      "enable": ["hitls_bsl", "hitls_crypto", "hitls_tls", "hitls_pki"],
      "features": {
        "hitls_bsl": ["err", "sal", "log", "hash", "base64", "pem"],
        "hitls_crypto": [
          "sha256", "sha384", "aes", "chacha20", "rsa", "ecdsa", "ecdh", "x25519",
          "hmac", "hkdf", "pbkdf2", "drbg", "gcm", "chacha20poly1305"
        ],
        "hitls_tls": [
          "proto_tls13", "proto_tls12", "host_server",
          "feature_session", "feature_alpn", "feature_sni",
          "suite_aes_256_gcm_sha384",
          "suite_chacha20_poly1305_sha256"
        ],
        "hitls_pki": ["x509_crt", "x509_vfy"]
      },
      "compile": {
        "optimization": "-O2",
        "security": ["-fPIC", "-fstack-protector-strong", "-D_FORTIFY_SOURCE=2"]
      },
      "asm": "x8664"
    }

Sources:
[config/json/feature.json1-631](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/feature.json#L1-L631)
[config/json/compile.json1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json#L1-L53)

## 6\. Troubleshooting Configuration Issues

Common configuration issues and their solutions:

Issue| Solution  
---|---  
Missing dependency| Check feature dependencies in `feature.json` and ensure
all required features are enabled  
Compilation errors| Verify compiler flags are compatible with your environment  
Performance issues| Enable architecture-specific optimizations and check
optimization flags  
Handshake failures| Ensure compatible TLS versions and cipher suites are
configured  
Memory constraints| Use minimal feature set and `-Os` optimization for size-
constrained environments  
  
For detailed error information, analyze the logs and error codes returned by
the library functions.

Sources:
[include/tls/hitls_error.h33-416](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_error.h#L33-L416)
[docs/en/4_User Guide/1_Build and Installation
Guide.md1-8024](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User
Guide/1_Build and Installation Guide.md#L1-L8024)

# Assembly Optimizations

Relevant source files

  * [.github/workflows/cmake-single-platform.yml](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-single-platform.yml)
  * [README-zh.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README-zh.md)
  * [README.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md)
  * [config/json/compile.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/compile.json)
  * [config/json/complete_options.json](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/json/complete_options.json)
  * [config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)
  * [crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)
  * [crypto/eal/src/eal_pkey_method.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_method.c)
  * [crypto/eal/src/eal_pkey_sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_sign.c)
  * [crypto/ealinit/src/asmcap_alg_asm.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_alg_asm.c)
  * [crypto/ealinit/src/asmcap_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h)
  * [crypto/ealinit/src/crypt_init.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c)
  * [crypto/include/crypt_arm.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_arm.h)
  * [crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)
  * [crypto/rsa/src/rsa_keyop.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_keyop.c)
  * [crypto/sha1/src/noasm_sha1.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1.c)
  * [crypto/sha1/src/noasm_sha1_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha1/src/noasm_sha1_small.c)
  * [crypto/sha2/src/noasm_sha256.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256.c)
  * [crypto/sha2/src/noasm_sha256_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256_small.c)
  * [crypto/sha2/src/noasm_sha512.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512.c)
  * [crypto/sha2/src/noasm_sha512_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha512_small.c)
  * [crypto/sm3/src/noasm_sm3.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sm3/src/noasm_sm3.c)
  * [docs/en/4_User Guide/1_Build and Installation Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/4_User Guide/1_Build and Installation Guide.md)
  * [docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md)
  * [include/crypto/crypt_eal_init.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h)
  * [testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c)
  * [testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c)

This page documents the assembly optimization mechanisms in openHiTLS, which
are used to enhance performance of cryptographic operations on supported CPU
architectures. Assembly optimizations provide significant performance
improvements compared to generic C implementations while maintaining the same
functionality and security guarantees.

For information about general build configuration options, see [Configuration
Options](/openHiTLS/openHiTLS/5.2-configuration-options).

## Overview of Assembly Optimizations

The openHiTLS library includes hand-optimized assembly implementations for
performance-critical cryptographic primitives on x86_64 and AArch64
architectures. These optimizations leverage CPU-specific instructions to
accelerate operations such as encryption/decryption, hashing, and big number
arithmetic.

    
    
    Optimized Algorithms
    
    Supported Architectures
    
    Assembly Optimizations
    
    CPU Architecture Detection
    
    Assembly Implementation Selection
    
    Fallback Mechanism
    
    x86_64
    
    AArch64 (ARM v8)
    
    Symmetric Encryption (AES, SM4, ChaCha20)
    
    Hash Functions (SHA1/2/3, SM3, MD5)
    
    Asymmetric Crypto (RSA, ECC)
    
    AEAD Modes (GCM, ChaCha20Poly1305)

Sources:
[config/macro_config/hitls_config_layer_crypto.h670-752](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L670-L752)
[crypto/ealinit/src/crypt_init.c270-449](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L270-L449)

## Supported CPU Architectures

openHiTLS currently provides assembly optimizations for the following
architectures:

Architecture| Supported Features| Configuration Flag  
---|---|---  
x86_64| AVX, BMI1, MOVBE| `--asm_type x8664`  
AArch64| NEON, AES, CRYPTO| `--asm_type armv8`  
  
The library automatically detects CPU capabilities at runtime to determine
which optimized implementations are available.

Sources:
[crypto/ealinit/src/asmcap_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h)
[README.md84-86](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L84-L86)

## Optimized Cryptographic Algorithms

The following cryptographic algorithms have assembly-optimized
implementations:

### Symmetric Encryption

Algorithm| x86_64| AArch64| Optimization Macro  
---|---|---|---  
AES| ✓| ✓| `HITLS_CRYPTO_AES_ASM`  
SM4| ✓| ✓| `HITLS_CRYPTO_SM4_ASM`  
ChaCha20| ✓| ✓| `HITLS_CRYPTO_CHACHA20_ASM`  
  
### Hash Functions

Algorithm| x86_64| AArch64| Optimization Macro  
---|---|---|---  
SHA-1| ✓| ✓| `HITLS_CRYPTO_SHA1_ASM`  
SHA-2 (224/256/384/512)| ✓| ✓| `HITLS_CRYPTO_SHA2_ASM`  
SM3| ✓| ✓| `HITLS_CRYPTO_SM3_ASM`  
MD5| ✓| ×| `HITLS_CRYPTO_MD5_ASM`  
  
### Asymmetric Cryptography

Algorithm| x86_64| AArch64| Optimization Macro  
---|---|---|---  
Big Number (BN)| ✓| ✓| `HITLS_CRYPTO_BN_ASM`  
NIST P-256| ✓| ✓| `HITLS_CRYPTO_CURVE_NISTP256_ASM`  
SM2| ✓| ✓| `HITLS_CRYPTO_CURVE_SM2_ASM`  
  
### AEAD Modes

Algorithm| x86_64| AArch64| Optimization Macro  
---|---|---|---  
GCM| ✓| ✓| `HITLS_CRYPTO_GCM_ASM`  
ChaCha20Poly1305| ✓| ✓| `HITLS_CRYPTO_CHACHA20POLY1305_ASM`  
  
Sources:
[config/macro_config/hitls_config_layer_crypto.h670-752](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h#L670-L752)
[crypto/ealinit/src/crypt_init.c270-449](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L270-L449)

## Runtime Selection Mechanism

openHiTLS implements a runtime detection mechanism that checks CPU features
and selects the appropriate implementation (assembly or C) for each algorithm.
This approach ensures maximum performance while maintaining portability.

    
    
    Required Features  
    Present
    
    Required Features  
    Not Present
    
    Memory Constrained
    
    Memory Available
    
    Algorithm Request
    
    CPU Feature  
    Detection
    
    Assembly Implementation
    
    C Implementation
    
    Small Memory  
    Optimized Implementation
    
    Standard C  
    Implementation
    
    Cryptographic Operation

The decision process is managed by the `CRYPT_ASMCAP_*` functions which
validate whether the required CPU features are available for each algorithm's
assembly implementation.

Sources:
[crypto/ealinit/src/crypt_init.c253-412](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L253-L412)
[crypto/ealinit/src/asmcap_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/asmcap_local.h)

## CPU Capability Detection

The system detects CPU capabilities through architecture-specific functions:

    
    
    x86_64
    
    AArch64
    
    GetCpuInstrSupportState()
    
    Architecture
    
    Check x86 Features  
    - AVX  
    - BMI1  
    - MOVBE
    
    Check ARM Features  
    - NEON  
    - AES  
    - CRYPTO
    
    Set Global Capability Flags
    
    Algorithm-specific  
    ASM checks

For each supported algorithm, there's an assembly capability check function
that determines whether the required CPU features are available. If any
required feature is missing, the system falls back to C implementations.

Sources:
[crypto/ealinit/src/crypt_init.c202-452](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L202-L452)
[testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c43-67](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/ealinit/test_suite_sdv_ealinit.c#L43-L67)

## Assembly Implementation Examples

Let's explore how different cryptographic algorithms are optimized in
assembly:

### Hash Functions

For hash functions like SHA-256, assembly optimizations typically focus on:

  * Optimizing message schedule computation
  * Implementing multiple rounds in parallel
  * Utilizing SIMD instructions for data processing

When assembly optimization isn't available or is explicitly disabled, the
system falls back to C implementations which may include both standard and
memory-optimized versions:

  * Standard C implementation: [crypto/sha2/src/noasm_sha256.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256.c)
  * Small memory C implementation: [crypto/sha2/src/noasm_sha256_small.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/sha2/src/noasm_sha256_small.c)

Similar patterns exist for other hash functions like SHA-1, SHA-512, and SM3.

### Symmetric Encryption

For symmetric encryption algorithms like AES, assembly optimizations include:

  * Using AES-NI instructions on x86_64
  * Leveraging NEON crypto extensions on AArch64
  * Optimizing key expansion and round operations

The AES implementation includes lookup tables when using the C implementation:
[crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)

## Enabling/Disabling Assembly Optimizations

Assembly optimizations can be enabled or disabled through the build
configuration system:

  1. **Build-time configuration** :

     * Use `--asm_type x8664` or `--asm_type armv8` during configuration
     * Define macros like `HITLS_CRYPTO_ASM_CHECK`
  2. **Runtime detection** :

     * Set to automatically detect and use available optimizations
     * Can be controlled via `CRYPT_EAL_Init` with `CRYPT_EAL_INIT_CPU` flag

Example configuration command to enable x86_64 assembly optimizations:

    
    
    python3 ../configure.py --enable hitls_bsl hitls_crypto hitls_tls hitls_pki hitls_auth --lib_type static --bits=64 --system=linux --asm_type x8664

Sources:
[README.md83-86](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/README.md#L83-L86)
[.github/workflows/cmake-single-
platform.yml31](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L31-L31)
[crypto/ealinit/src/crypt_init.c176-198](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L176-L198)

## Performance Considerations

Assembly optimizations can provide significant performance improvements:

  * Symmetric encryption (AES, SM4): 3-10× faster
  * Hash functions (SHA-2, SM3): 2-5× faster
  * Asymmetric operations (RSA, ECC): 1.5-3× faster

The performance gains vary based on:

  * CPU architecture and available instructions
  * Algorithm and key size
  * Input data size
  * Operation type (encryption/decryption/signing/verification)

## Integration with the Provider Framework

The assembly optimization system integrates with the Provider Framework
through CPU capability detection:

    
    
    Yes
    
    No
    
    CRYPT_EAL_Init()
    
    CRYPT_EAL_INIT_CPU  
    flag set?
    
    GetCpuInstrSupportState()
    
    Skip CPU Detection
    
    Initialize EAL Providers
    
    Provider selection  
    with ASM capability
    
    ASM-optimized operations

When initializing the cryptographic engine with `CRYPT_EAL_Init`, setting the
`CRYPT_EAL_INIT_CPU` flag enables CPU capability detection, which influences
the provider selection process to favor assembly-optimized implementations
when available.

Sources:
[crypto/ealinit/src/crypt_init.c176-226](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/ealinit/src/crypt_init.c#L176-L226)
[include/crypto/crypt_eal_init.h34-39](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h#L34-L39)

## Troubleshooting

If you encounter issues with assembly optimizations:

  1. **Verify CPU support** : Ensure your CPU supports the required features (AVX, NEON, etc.)
  2. **Check build configuration** : Verify assembly optimizations are enabled (`--asm_type`)
  3. **Enable runtime checks** : Use `HITLS_CRYPTO_ASM_CHECK` to verify capability detection
  4. **Force C implementation** : Disable assembly optimizations if needed

## Conclusion

Assembly optimizations in openHiTLS provide significant performance
improvements for cryptographic operations on supported architectures. The
system's dynamic selection mechanism ensures optimal performance while
maintaining compatibility across different platforms.

For developers, these optimizations are transparent and require no code
changes, as the system automatically selects the best implementation based on
CPU capabilities.

# Developer Guides

Relevant source files

  * [crypto/drbg/include/crypt_drbg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/include/crypt_drbg.h)
  * [crypto/eal/src/eal_md.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c)
  * [crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
  * [crypto/hybridkem/include/crypt_hybridkem.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/include/crypt_hybridkem.h)
  * [crypto/include/crypt_local_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_local_types.h)
  * [crypto/provider/src/mgr/crypt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c)
  * [docs/en/5_Developer Guide/4_provider Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md)
  * [docs/index/index.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/index/index.md)
  * [include/crypto/crypt_eal_implprovider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h)
  * [include/crypto/crypt_eal_rand.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_rand.h)
  * [include/crypto/crypt_errno.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h)
  * [include/crypto/crypt_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_types.h)
  * [testcode/demo/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt)
  * [testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
  * [testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c)
  * [testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)
  * [testcode/demo/privpass_token.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c)
  * [testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
  * [testcode/demo/sm2enc.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c)
  * [testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c)
  * [testcode/script/execute_sdv.sh](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/script/execute_sdv.sh)
  * [testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c)
  * [testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c)

This document provides comprehensive guidance for developers working with the
openHiTLS codebase. It covers how to understand the system architecture,
develop custom cryptographic providers, effectively test the software, and
integrate openHiTLS into your applications.

For specific topics not covered in depth here, refer to these related
documents:

  * For API reference information, see [API Reference](/openHiTLS/openHiTLS/3-cryptographic-services)
  * For application-specific security guidance, see [Secure Communication Application Development Guide](/openHiTLS/openHiTLS/2-architecture)

## System Architecture Overview

When developing with openHiTLS, it's essential to understand how the key
architectural components interact. The system employs a modular, layered
design that enables extensibility and clear separation of concerns.

    
    
    Basic Support Layer (BSL)
    
    Applications
    
    TLS Protocol Layer
    
    Cryptographic Services Layer
    
    Provider Framework
    
    Logging
    
    Memory Management
    
    OS Abstraction
    
    I/O Handling
    
    ASN.1/PEM Encoding
    
    PKI/X.509
    
    Default Provider
    
    Custom Providers

This architecture consists of:

  1. **TLS Protocol Layer** : Implements TLS handshake, record protocols, and other TLS-specific functionality
  2. **Cryptographic Services Layer** : Provides cryptographic primitives through the Ecosystem Abstraction Layer (EAL)
  3. **Provider Framework** : Manages and abstracts different implementations of cryptographic algorithms
  4. **Basic Support Layer** : Provides foundational services like logging, memory management, and I/O handling

Sources: `crypto/eal/src/eal_rand.c`, `include/crypto/crypt_types.h`,
`include/crypto/crypt_eal_implprovider.h`

## Provider Framework

The Provider Framework is a core extension mechanism in openHiTLS, allowing
for dynamic loading, management, and selection of cryptographic
implementations.

    
    
    Provider Framework
    
    Provider Manager
    
    Provider Loading/Unloading
    
    Algorithm Discovery
    
    Provider Selection
    
    Default Provider
    
    Dynamic Loading
    
    Algorithm Capabilities Query
    
    Scoring/Prioritization
    
    Default Implementations
    
    Custom Implementations
    
    Hardware-optimized Implementations
    
    Generic Implementations

### Key Components

  * **Library Context (`CRYPT_EAL_LibCtx`)**: Manages the lifecycle and resources of all loaded providers
  * **Provider Manager Context (`CRYPT_EAL_ProvMgrCtx`)**: Represents a single provider, including its loaded library handle and implemented functionalities
  * **Functional Interfaces** : Standardized functions for querying and invoking provider operations

For detailed information on developing custom providers, see [Provider
Development Guide](/openHiTLS/openHiTLS/4-tls-protocol-implementation).

Sources: `docs/en/5_Developer Guide/4_provider Development Guide.md`,
`include/crypto/crypt_eal_implprovider.h`

## Testing Framework

openHiTLS includes a comprehensive testing framework to verify the library's
correctness and security. The testing framework is designed to be both
thorough and flexible.

    
    
    execute_sdv.sh
    
    Test Selection
    
    Run All Tests
    
    Run Specific Test Suites
    
    Run Specific Test Cases
    
    Execution Mode
    
    Concurrent Execution
    
    Sequential Execution
    
    Test Reports
    
    Pass/Fail/Skip Counts
    
    ASAN Checks
    
    Execution Time

### Writing Tests

Tests in openHiTLS are organized into test suites, with each suite containing
multiple test cases targeting specific functionality. The testing framework
uses a structure similar to other unit testing frameworks:

  1. Test suites are defined in files named `test_suite_*.c`
  2. Each test case is a function within the test suite
  3. Test cases use assertion macros to verify expected behavior

### Running Tests

Tests can be run using the `execute_sdv.sh` script with the following options:

  * `-c`: Run tests concurrently
  * `-p <number>`: Specify number of concurrent processes
  * `-s <test_suite>`: Run a specific test suite
  * `-g <function_name>`: Run a specific test case

    
    
    # Run all tests concurrently
    ./execute_sdv.sh -c
    
    # Run a specific test suite
    ./execute_sdv.sh -s test_suite_sdv_eal_provider_load
    
    # Run a specific test case
    ./execute_sdv.sh -s test_suite_sdv_eal_aes -g test_aes_cbc_encrypt

The script handles setting up the environment, running tests, and generating
comprehensive test reports.

Sources: `testcode/script/execute_sdv.sh`,
`testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c`,
`testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c`

## Integration Patterns

When integrating openHiTLS into your applications, follow these common
patterns observed in the example code.

    
    
    Initialize BSL Error Handling
    
    Register Memory Management Callbacks
    
    Initialize EAL
    
    Initialize Random Number Generator
    
    Perform Cryptographic Operations
    
    Clean Up Resources

### Standard Integration Process

  1. **Initialize the BSL error handling** :
         
         BSL_ERR_Init();

  2. **Set up memory management callbacks** :
         
         BSL_SAL_CallBack_Ctrl(BSL_SAL_MEM_MALLOC_CB_FUNC, StdMalloc);
         BSL_SAL_CallBack_Ctrl(BSL_SAL_MEM_FREE_CB_FUNC, free);

  3. **Initialize the EAL** :
         
         ret = CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);

  4. **Initialize the random number generator** :
         
         ret = CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);

  5. **Perform cryptographic operations specific to your use case**

  6. **Clean up resources** :
         
         CRYPT_EAL_RandDeinit();
         BSL_ERR_DeInit();

Sources: `testcode/demo/client.c`, `testcode/demo/server.c`,
`testcode/demo/drbg.c`

### Example: Client-Server TLS Communication

The following table summarizes the key steps in setting up client-server TLS
communication:

Client Side| Server Side  
---|---  
Initialize BSL and EAL| Initialize BSL and EAL  
Create socket and connect| Create socket, bind, and listen  
Create TLS config| Create TLS config  
Load certificates| Load certificates and private key  
Create TLS context| Create TLS context  
Perform TLS handshake (`HITLS_Connect`)| Accept connection (`HITLS_Accept`)  
Send/receive data| Send/receive data  
Close connection and clean up| Close connection and clean up  
  
See `testcode/demo/client.c` and `testcode/demo/server.c` for complete
examples.

Sources: `testcode/demo/client.c`, `testcode/demo/server.c`

## Working with Cryptographic Operations

openHiTLS provides a comprehensive set of cryptographic operations. Below are
examples of common operations:

### Random Number Generation

    
    
    uint8_t output[100] = {0};
    uint32_t len = 100;
    
    // Initialize the random number generator
    ret = CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Generate random bytes
    ret = CRYPT_EAL_RandbytesEx(NULL, output, len);
    
    // Optional: Reseed the random number generator
    ret = CRYPT_EAL_RandSeedEx(NULL);

Sources: `testcode/demo/drbg.c`, `crypto/eal/src/eal_rand.c`

### Digital Signatures with SM2

    
    
    // Create SM2 context
    CRYPT_EAL_PkeyCtx *ctx = CRYPT_EAL_PkeyNewCtx(CRYPT_PKEY_SM2);
    
    // Set user ID for SM2
    ret = CRYPT_EAL_PkeyCtrl(ctx, CRYPT_CTRL_SET_SM2_USER_ID, userId, sizeof(userId));
    
    // Generate key pair
    ret = CRYPT_EAL_PkeyGen(ctx);
    
    // Sign data
    ret = CRYPT_EAL_PkeySign(ctx, CRYPT_MD_SM3, msg, sizeof(msg), signBuf, &signLen);
    
    // Verify signature
    ret = CRYPT_EAL_PkeyVerify(ctx, CRYPT_MD_SM3, msg, sizeof(msg), signBuf, signLen);

Sources: `testcode/demo/sm2sign.c`

### Key Exchange with ECDH

    
    
    // Create ECDH contexts
    CRYPT_EAL_PkeyCtx *localCtx = CRYPT_EAL_PkeyNewCtx(CRYPT_PKEY_ECDH);
    CRYPT_EAL_PkeyCtx *peerCtx = CRYPT_EAL_PkeyNewCtx(CRYPT_PKEY_ECDH);
    
    // Set parameters (curve) for ECDH
    ret = CRYPT_EAL_PkeySetParaById(localCtx, CRYPT_PKEY_PARA_SECP256R1);
    
    // Set keys
    ret = CRYPT_EAL_PkeySetPrivateKey(localCtx, localPrivKey, localPrivKeyLen);
    ret = CRYPT_EAL_PkeySetPublicKey(peerCtx, peerPubKey, peerPubKeyLen);
    
    // Compute shared secret
    ret = CRYPT_EAL_PkeyComputeKey(localCtx, peerCtx, sharedSecret, &sharedSecretLen);

Sources: `testcode/demo/ecdh.c`

## Error Handling Best Practices

Proper error handling is crucial for building robust applications with
openHiTLS. The library uses an extensive error code system defined in
`crypt_errno.h`.

    
    
    == CRYPT_SUCCESS
    
    != CRYPT_SUCCESS
    
    Function Call
    
    Check Return Value
    
    Continue Processing
    
    Handle Error
    
    Get Error Details
    
    Clean Up Resources
    
    Report Error

### Error Check Pattern

    
    
    ret = CRYPT_EAL_Function();
    if (ret != CRYPT_SUCCESS) {
        // Handle error
        const char *file = NULL;
        uint32_t line = 0;
        BSL_ERR_GetLastErrorFileLine(&file, &line);
        printf("Error occurred in %s at line %d with code 0x%x\n", file, line, ret);
        
        // Clean up resources
        // ...
        
        return ret;
    }

### Key Error Codes

  * `CRYPT_SUCCESS`: Operation completed successfully
  * `CRYPT_NULL_INPUT`: Null pointer input error
  * `CRYPT_MEM_ALLOC_FAIL`: Memory allocation failure
  * `CRYPT_NOT_SUPPORT`: Unsupported operation
  * `CRYPT_EAL_ERR_ALGID`: Incorrect algorithm ID

For a complete list of error codes, refer to `include/crypto/crypt_errno.h`.

Sources: `include/crypto/crypt_errno.h`, various demo files

## Additional Resources

The following demo files provide complete examples of various operations:

  1. **TLS Client/Server** : `testcode/demo/client.c` and `testcode/demo/server.c`
  2. **Random Number Generation** : `testcode/demo/drbg.c`
  3. **Key Exchange** : `testcode/demo/ecdh.c`
  4. **Digital Signatures** : `testcode/demo/sm2sign.c`
  5. **Encryption/Decryption** : `testcode/demo/sm2enc.c`, `testcode/demo/sm4cbc.c`
  6. **Authentication Tokens** : `testcode/demo/privpass_token.c`

These examples can be built using the CMake configuration in
`testcode/demo/CMakeLists.txt`.

Sources: `testcode/demo/CMakeLists.txt` and various demo files

# Creating Custom Providers

Relevant source files

  * [crypto/drbg/include/crypt_drbg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/include/crypt_drbg.h)
  * [crypto/drbg/src/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/src/drbg.c)
  * [crypto/eal/src/eal_md.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c)
  * [crypto/eal/src/eal_pkey_gen.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_gen.c)
  * [crypto/hybridkem/include/crypt_hybridkem.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/include/crypt_hybridkem.h)
  * [crypto/include/crypt_local_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/include/crypt_local_types.h)
  * [crypto/provider/src/default/crypt_default_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/default/crypt_default_rand.c)
  * [crypto/provider/src/mgr/crypt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c)
  * [docs/en/5_Developer Guide/4_provider Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md)
  * [docs/index/index.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/index/index.md)
  * [include/crypto/crypt_eal_implprovider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h)
  * [include/crypto/crypt_eal_pkey.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_pkey.h)
  * [include/crypto/crypt_eal_rand.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_rand.h)
  * [include/crypto/crypt_errno.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_errno.h)
  * [include/crypto/crypt_types.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_types.h)
  * [testcode/script/execute_sdv.sh](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/script/execute_sdv.sh)
  * [testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.c)
  * [testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/drbg/test_suite_sdv_drbg.data)
  * [testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c)

This document provides a comprehensive guide on how to create custom
cryptographic providers for the openHiTLS project. Custom providers allow you
to extend openHiTLS with your own cryptographic implementations, hardware-
accelerated algorithms, or specialized cryptographic services. For information
about using existing providers, see [Provider Framework
Architecture](/openHiTLS/openHiTLS/2.1-provider-framework).

## Introduction to the Provider Framework

The openHiTLS Provider Framework enables dynamic loading, management, and
usage of cryptographic implementations. Each provider is a modular component
that encapsulates a specific set of cryptographic operations and exposes them
through standardized interfaces.

    
    
    Provider Selection Process
    
    Application
    
    openHiTLS API
    
    Provider Framework
    
    Default Provider
    
    Custom Provider 1
    
    Custom Provider 2
    
    Algorithm  
    Discovery
    
    Scoring  
    Mechanism
    
    Provider  
    Loading
    
    Hardware-optimized  
    Implementations
    
    Generic  
    Implementations
    
    Provider-specific  
    Implementations
    
    Provider-specific  
    Implementations

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md15-134](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L15-L134)
  * [include/crypto/crypt_eal_implprovider.h15-283](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h#L15-L283)

## Core Provider Framework Concepts

The provider framework is built around several key concepts:

  1. **Library Context** (`CRYPT_EAL_LibCtx`): Manages the lifecycle and resources of all loaded providers.
  2. **Provider Manager Context** (`CRYPT_EAL_ProvMgrCtx`): Represents a single provider, including its loaded library handle and implemented functionalities.
  3. **Functional Interfaces** : Standardized functions used for querying and invoking specific operations of providers.
  4. **Algorithm Registry** : Each provider registers its supported algorithms with specific attributes.

    
    
    contains
    
    exposes
    
    1
    
    1
    
    *
    
    *
    
    CRYPT_EAL_LibCtx
    
    +providers: List
    
    +searchProviderPath: String
    
    +lock: ThreadLockHandle
    
    +drbg: Pointer
    
    CRYPT_EAL_ProvMgrCtx
    
    +name: String
    
    +library: Handle
    
    +providerInit: Function
    
    +provCtx: Pointer
    
    +funcProvQuery: Function
    
    +funcProvCtrl: Function
    
    +funcProvFree: Function
    
    +ref: Counter
    
    CRYPT_EAL_AlgInfo
    
    +algId: int32_t
    
    +implFunc: CRYPT_EAL_Func
    
    +attr: char

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md10-13](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L10-L13)
  * [crypto/provider/src/mgr/crypt_provider.c40-67](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c#L40-L67)
  * [include/crypto/crypt_eal_implprovider.h37-41](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h#L37-L41)

## Provider Initialization

When creating a custom provider, you must implement a mandatory initialization
function named `CRYPT_EAL_ProviderInit`. This function is called by the
framework when the provider is loaded:

    
    
    Custom ProviderDynamic LibraryProvider FrameworkApplicationCustom ProviderDynamic LibraryProvider FrameworkApplicationCRYPT_EAL_ProviderLoad()dlopen()Handledlsym("CRYPT_EAL_ProviderInit")Init FunctionCRYPT_EAL_ProviderInit()Initialize providerRegister algorithmsReturn outFuncs arrayStore provider infoSuccess

The initialization function must have this signature:

    
    
    int32_t CRYPT_EAL_ProviderInit(
        CRYPT_EAL_ProvMgrCtx *mgrCtx,
        BSL_Param *param,
        CRYPT_EAL_Func *capFuncs,
        CRYPT_EAL_Func **outFuncs,
        void **provCtx
    );

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md284-330](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L284-L330)
  * [include/crypto/crypt_eal_implprovider.h92-105](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h#L92-L105)
  * [crypto/provider/src/mgr/crypt_provider.c33-86](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c#L33-L86)

## Creating a Custom Provider

### Step 1: Define Your Provider Structure

Start by defining a structure to hold your provider-specific data. This is
optional but recommended for providers that need to maintain state.

    
    
    typedef struct {
        /* Provider-specific data */
        void *entropy_source;
        /* Other implementation-specific fields */
    } MY_PROVIDER_CTX;

### Step 2: Implement Algorithm Functions

Implement the cryptographic algorithms your provider will support. Each
operation type (symmetric ciphers, hash functions, etc.) has its own set of
function definitions in `crypt_eal_implprovider.h`.

For example, if you're implementing a digest algorithm:

    
    
    void *MY_PROVIDER_MdNewCtx(void *provCtx, int32_t algId)
    {
        /* Allocate and initialize algorithm context */
    }
    
    int32_t MY_PROVIDER_MdInit(void *ctx, const BSL_Param *param)
    {
        /* Initialize digest operation */
    }
    
    int32_t MY_PROVIDER_MdUpdate(void *ctx, const uint8_t *input, uint32_t len)
    {
        /* Process data */
    }
    
    int32_t MY_PROVIDER_MdFinal(void *ctx, uint8_t *out, uint32_t *outLen)
    {
        /* Finalize digest and output result */
    }
    
    void MY_PROVIDER_MdFreeCtx(void *ctx)
    {
        /* Free resources */
    }

### Step 3: Define Algorithm Info Structures

Create structures that define the algorithms your provider implements:

    
    
    static const CRYPT_EAL_Func myMdSha256[] = {
        {CRYPT_EAL_IMPLMD_NEWCTX, MY_PROVIDER_MdNewCtx},
        {CRYPT_EAL_IMPLMD_INITCTX, MY_PROVIDER_MdInit},
        {CRYPT_EAL_IMPLMD_UPDATE, MY_PROVIDER_MdUpdate},
        {CRYPT_EAL_IMPLMD_FINAL, MY_PROVIDER_MdFinal},
        {CRYPT_EAL_IMPLMD_FREECTX, MY_PROVIDER_MdFreeCtx},
        /* Other functions as needed */
        CRYPT_EAL_FUNC_END  /* Marks the end of the array */
    };
    
    static const CRYPT_EAL_AlgInfo myDigests[] = {
        {CRYPT_MD_SHA256, myMdSha256, "name=sha256,provider=myprovider,version=1.0"},
        /* Other algorithms */
        CRYPT_EAL_ALGINFO_END  /* Marks the end of the array */
    };

The attribute string (`"name=sha256,provider=myprovider,version=1.0"`) is used
for algorithm discovery and selection.

### Step 4: Implement Query Function

Create a function that returns the algorithms supported by your provider:

    
    
    static int32_t MY_PROVIDER_Query(void *provCtx, int32_t operaId, CRYPT_EAL_AlgInfo **algInfos)
    {
        (void)provCtx;  /* May use provCtx if needed */
        
        switch (operaId) {
            case CRYPT_EAL_OPERAID_HASH:
                *algInfos = myDigests;
                return CRYPT_SUCCESS;
            /* Other operation types */
            default:
                return CRYPT_NOT_SUPPORT;
        }
    }

### Step 5: Implement Provider Init Function

Implement the main provider initialization function:

    
    
    int32_t CRYPT_EAL_ProviderInit(
        CRYPT_EAL_ProvMgrCtx *mgrCtx,
        BSL_Param *param,
        CRYPT_EAL_Func *capFuncs,
        CRYPT_EAL_Func **outFuncs,
        void **provCtx
    )
    {
        /* Use capabilities from framework if needed */
        CRYPT_RandSeedMethod entropy = {0};
        int32_t index = 0;
        
        while (capFuncs[index].id != 0) {
            switch (capFuncs[index].id) {
                case CRYPT_EAL_CAP_GETENTROPY:
                    entropy.getEntropy = capFuncs[index].func;
                    break;
                /* Other capabilities */
            }
            index++;
        }
        
        /* Create provider context if needed */
        MY_PROVIDER_CTX *myCtx = malloc(sizeof(MY_PROVIDER_CTX));
        if (myCtx == NULL) {
            return CRYPT_MEM_ALLOC_FAIL;
        }
        
        /* Initialize provider context */
        
        /* Set output functions */
        static CRYPT_EAL_Func provOutFuncs[] = {
            {CRYPT_EAL_PROVCB_QUERY, MY_PROVIDER_Query},
            {CRYPT_EAL_PROVCB_FREE, MY_PROVIDER_Free},
            {CRYPT_EAL_PROVCB_CTRL, MY_PROVIDER_Ctrl},
            CRYPT_EAL_FUNC_END
        };
        
        *outFuncs = provOutFuncs;
        *provCtx = myCtx;
        
        return CRYPT_SUCCESS;
    }

### Step 6: Implement Cleanup Function

If your provider uses a provider context, implement a cleanup function:

    
    
    static void MY_PROVIDER_Free(void *provCtx)
    {
        if (provCtx != NULL) {
            MY_PROVIDER_CTX *myCtx = (MY_PROVIDER_CTX *)provCtx;
            /* Clean up resources */
            free(myCtx);
        }
    }

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md329-436](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L329-L436)
  * [include/crypto/crypt_eal_implprovider.h107-278](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h#L107-L278)

## Provider Loading and Selection

### Loading a Custom Provider

Applications load your provider using:

    
    
    CRYPT_EAL_LibCtx *libCtx = CRYPT_EAL_LibCtxNew();
    CRYPT_EAL_ProviderSetLoadPath(libCtx, "/path/to/providers");
    CRYPT_EAL_ProviderLoad(libCtx, BSL_SAL_CONVERTER_SO, "myprovider", NULL, NULL);

### Provider Selection Mechanism

When an algorithm is requested, the framework searches for matching
implementations based on algorithm ID and optional attributes:

    
    
    Yes
    
    No
    
    Yes
    
    No
    
    Application  
    Requests Algorithm
    
    Is LibCtx  
    Specified?
    
    Use Specified LibCtx
    
    Use Global LibCtx
    
    Search for Matching  
    Algorithm ID
    
    Is Search  
    String NULL?
    
    Return First  
    Matching Algorithm
    
    Apply Scoring  
    Mechanism
    
    Return Best  
    Matching Algorithm

The provider selection uses a scoring mechanism based on attribute matching:

Operator| Meaning| Effect on Score  
---|---|---  
`=`| Must be equal| Mandatory condition  
`!=`| Must not be equal| Mandatory condition  
`?`| Optional match| +1 per match  
  
For example, the search string `"name=sha256,provider?myprovider,version?1.0"`
requires the name to be "sha256" and gives preference to providers named
"myprovider" with version "1.0".

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md213-279](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L213-L279)
  * [crypto/provider/src/mgr/crypt_provider.c80-146](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c#L80-L146)

## Provider Capabilities

Providers can declare their capabilities to the framework, which are used for
features like TLS handshakes:

### Group Capabilities

Providers can declare supported key exchange or key encapsulation mechanism
(KEM) groups for TLS:

    
    
    static int32_t MY_PROVIDER_GetCaps(void *provCtx, int32_t cmd, CRYPT_EAL_ProcCapsCb cb, void *args)
    {
        if (cmd == CRYPT_EAL_GET_GROUP_CAP) {
            BSL_Param group[] = {
                {CRYPT_PARAM_CAP_TLS_GROUP_IANA_GROUP_NAME, BSL_PARAM_TYPE_OCTETS_PTR, "x25519", 0, 0},
                {CRYPT_PARAM_CAP_TLS_GROUP_IANA_GROUP_ID, BSL_PARAM_TYPE_UINT16, &groupId, sizeof(groupId), 0},
                {CRYPT_PARAM_CAP_TLS_GROUP_PARA_ID, BSL_PARAM_TYPE_INT32, &paraId, sizeof(paraId), 0},
                {CRYPT_PARAM_CAP_TLS_GROUP_ALG_ID, BSL_PARAM_TYPE_INT32, &algId, sizeof(algId), 0},
                {CRYPT_PARAM_CAP_TLS_GROUP_SEC_BITS, BSL_PARAM_TYPE_INT32, &secBits, sizeof(secBits), 0},
                {CRYPT_PARAM_CAP_TLS_GROUP_VERSION_BITS, BSL_PARAM_TYPE_UINT32, &versionBits, sizeof(versionBits), 0},
                {CRYPT_PARAM_CAP_TLS_GROUP_IS_KEM, BSL_PARAM_TYPE_BOOL, &isKem, sizeof(isKem), 0},
                BSL_PARAM_END
            };
            return cb(args, group);
        }
        
        return CRYPT_NOT_SUPPORT;
    }

### Signature Algorithm Capabilities

Providers can also declare supported signature algorithms:

    
    
    if (cmd == CRYPT_EAL_GET_SIGALG_CAP) {
        BSL_Param sigAlg[] = {
            {CRYPT_PARAM_CAP_TLS_SIGNALG_IANA_SIGN_NAME, BSL_PARAM_TYPE_OCTETS_PTR, "ecdsa_secp256r1_sha256", 0, 0},
            {CRYPT_PARAM_CAP_TLS_SIGNALG_IANA_SIGN_ID, BSL_PARAM_TYPE_UINT16, &signId, sizeof(signId), 0},
            {CRYPT_PARAM_CAP_TLS_SIGNALG_KEY_TYPE, BSL_PARAM_TYPE_INT32, &keyType, sizeof(keyType), 0},
            /* Other parameters */
            BSL_PARAM_END
        };
        return cb(args, sigAlg);
    }

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md150-197](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L150-L197)

## Best Practices for Provider Development

  1. **Resource Management** : Always clean up resources properly in your provider. Implement cleanup functions for all contexts.

  2. **Thread Safety** : Ensure your provider is thread-safe, especially if it maintains global state.

  3. **Error Handling** : Return appropriate error codes from the `crypt_errno.h` header and use the `BSL_ERR_PUSH_ERROR` macro to report errors.

  4. **Descriptive Attributes** : Use clear and descriptive attributes for your algorithms to aid in discovery and selection.

  5. **Documentation** : Document your provider's capabilities, supported algorithms, and any special requirements or limitations.

  6. **Testing** : Create comprehensive tests for your provider to ensure it works correctly under various conditions.

  7. **Performance** : Consider performance implications, especially for cryptographic algorithms that may be called frequently.

  8. **Integration** : Test your provider's integration with the wider openHiTLS library to ensure compatibility.

## Example Workflow

The typical workflow for creating and using a custom provider is:

    
    
    ApplicationDeveloperApplicationDeveloperImplement provider functionsDefine algorithm informationImplement CRYPT_EAL_ProviderInitCompile as shared libraryCreate LibCtxSet provider pathLoad providerGet algorithm implementationUse algorithmUnload provider when done

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md437-511](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md#L437-L511)
  * [testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c57-146](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c#L57-L146)

## Conclusion

Creating custom providers for openHiTLS allows you to extend the library with
specialized cryptographic implementations. By following the structure and
interfaces defined by the provider framework, you can create providers that
seamlessly integrate with the rest of the library.

For more information on specific cryptographic algorithms and how to implement
them, refer to the related documentation sections and the header files in the
`include/crypto` directory.

Sources:

  * [docs/en/5_Developer Guide/4_provider Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md)
  * [include/crypto/crypt_eal_implprovider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_implprovider.h)
  * [crypto/provider/src/mgr/crypt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c)

# Testing Framework

Relevant source files

  * [.github/workflows/cmake-single-platform.yml](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-single-platform.yml)
  * [bsl/asn1/src/bsl_asn1_local.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/asn1/src/bsl_asn1_local.h)
  * [bsl/pem/include/bsl_pem_internal.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/pem/include/bsl_pem_internal.h)
  * [bsl/pem/src/bsl_pem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/pem/src/bsl_pem.c)
  * [bsl/sal/src/sal_file.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/bsl/sal/src/sal_file.c)
  * [crypto/aes/src/crypt_aes_tbox.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/aes/src/crypt_aes_tbox.c)
  * [crypto/eal/src/eal_pkey_method.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_method.c)
  * [crypto/eal/src/eal_pkey_sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_pkey_sign.c)
  * [crypto/hybridkem/include/crypt_hybridkem.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/hybridkem/include/crypt_hybridkem.h)
  * [crypto/provider/src/mgr/crypt_provider.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c)
  * [crypto/rsa/src/rsa_encdec.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_encdec.c)
  * [crypto/rsa/src/rsa_keyop.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/rsa/src/rsa_keyop.c)
  * [testcode/script/execute_sdv.sh](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/script/execute_sdv.sh)
  * [testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c)
  * [testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.data](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.data)
  * [testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/aes/test_suite_sdv_eal_aes.c)
  * [testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/entropy/test_suite_sdv_entropy.c)
  * [testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c)
  * [testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c)

The openHiTLS Testing Framework provides comprehensive testing capabilities
for validating the functionality, reliability, and security of the openHiTLS
cryptographic library. This page documents the framework's architecture,
components, and usage to help developers understand how tests are organized,
written, and executed.

## Overview

The openHiTLS Testing Framework consists of a collection of test suites that
collectively verify different aspects of the cryptographic library. It
includes API validation tests, functional correctness tests, error handling
tests, and integration tests. The framework is designed to be scalable,
allowing tests to be run in parallel, and is integrated with continuous
integration workflows.

    
    
    Testing Framework
    
    Test Suites
    
    Test Execution Scripts
    
    Test Data
    
    CI Integration
    
    Crypto Algorithm Tests
    
    Protocol Tests
    
    Provider Tests
    
    BSL Tests
    
    execute_sdv.sh
    
    build_sdv.sh
    
    Test Vectors
    
    Test Certificates
    
    GitHub Actions
    
    Coverage Analysis

Sources: [.github/workflows/cmake-single-
platform.yml1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L1-L53)
[testcode/script/execute_sdv.sh1-296](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/script/execute_sdv.sh#L1-L296)

## Test Suite Organization

Tests are organized into modular test suites, each focused on a specific
component or functionality of the library. The naming convention follows a
pattern of `test_suite_sdv_[component]_[feature].c`.

### Suite Structure

Each test suite consists of:

  1. **Header Section** : Includes necessary headers and utility functions
  2. **Test Cases** : Individual test functions with assertions
  3. **Test Data** : External data files for parameterized testing

Each test case follows a standard format:

    
    
    /**
     * @test   [TEST_ID]
     * @title  [Short description]
     * @precon [Prerequisites]
     * @brief  [Test steps and expectations]
     * @expect [Expected results]
     */
    /* BEGIN_CASE */
    void <FileRef file-url="https://github.com/openHiTLS/openHiTLS/blob/d4dca345/TEST_FUNCTION_NAME" undefined  file-path="TEST_FUNCTION_NAME">Hii</FileRef> {
        // Test setup
        // Test execution
        // Assertions
        // Cleanup
    EXIT:
        // Additional cleanup
    }
    /* END_CASE */
    
    
    
    Test Suite
    
    Header Section
    
    Test Cases
    
    Test Data File (.data)
    
    Test Case 1
    
    Test Case 2
    
    Test Case n
    
    Setup
    
    Execution
    
    Assertions
    
    Cleanup
    
    Test Vectors
    
    Parameters
    
    Expected Results

Sources:
[testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c15-678](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c#L15-L678)
[testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c15-112](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c#L15-L112)
[testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.data1-50](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.data#L1-L50)

## Test Execution Framework

The test execution is managed by shell scripts that handle test discovery,
execution, result collection, and reporting.

### Primary Components

  1. **execute_sdv.sh** : Main script for executing tests
  2. **build_sdv.sh** : Script for building the test environment
  3. **Test Binary** : Generated executable for each test suite

### Test Execution Flow

The typical flow of test execution is:

  1. Test binaries are built from test suite source files
  2. `execute_sdv.sh` discovers test binaries in the output directory
  3. Tests are executed either sequentially or in parallel
  4. Results are collected and verified
  5. Test report is generated

    
    
    ResultsTestBinariesexecute_sdv.shUserResultsTestBinariesexecute_sdv.shUseralt[Run specific tests][Run all tests]Run testsParse optionsSetup environmentExecute specific test suitesDiscover test binariesSetup parallel executionExecute tests in parallelGenerate test resultsCollect resultsCheck for ASAN errorsRun demo applicationsGenerate test reportReturn exit code

Sources:
[testcode/script/execute_sdv.sh53-192](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/script/execute_sdv.sh#L53-L192)
[.github/workflows/cmake-single-
platform.yml31-41](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L31-L41)

## Test Environment

The test environment provides necessary resources for tests to run correctly.

### Key Features

  1. **Environment Variables** : Set up paths to libraries and test data
  2. **ASAN Integration** : Address Sanitizer integration for memory error detection
  3. **Concurrent Execution** : Support for parallel test execution
  4. **CI Integration** : Integration with GitHub Actions workflow

### Test Reporting

After test execution, a comprehensive report is generated with:

  1. Total number of test cases
  2. Number of passed tests
  3. Number of skipped tests
  4. Number of failed tests
  5. Total execution time

Sources:
[testcode/script/execute_sdv.sh95-119](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/script/execute_sdv.sh#L95-L119)
[.github/workflows/cmake-single-
platform.yml38-52](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L38-L52)

## Writing Tests

This section describes how to write effective tests using the framework.

### Assertion Macros

The framework provides several assertion macros for validating test
conditions:

Macro| Description  
---|---  
`ASSERT_TRUE(condition)`| Verifies the condition is true  
`ASSERT_EQ(actual, expected)`| Verifies equality between actual and expected
values  
`ASSERT_TRUE_AND_LOG(message, condition)`| Verifies condition with a log
message  
`ASSERT_COMPARE(message, expected, expectedLen, actual, actualLen)`| Compares
memory blocks  
`ASSERT_EQ_LOG(message, actual, expected)`| Verifies equality with a log
message  
  
### Test Utilities

Common test utilities include:

  1. **TestMemInit()** : Initializes memory management for testing
  2. **SetRsaPrvKey()** , **SetRsaPubKey()** : Utilities for setting up RSA keys
  3. **Test*Ctx()** : Functions to create test contexts
  4. **TestRandInit()** : Initializes random generator for testing

### Parameterized Tests

Tests can be parameterized using test data files (`.data` files) which
contain:

  1. Test function name
  2. Test parameters
  3. Expected results

This allows the same test logic to be run with multiple inputs and expected
outcomes.

Sources:
[testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c32-56](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c#L32-L56)
[testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c28-111](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.c#L28-L111)
[testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.data1-50](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/bsl/pem/test_suite_sdv_pem.data#L1-L50)

## Test Types

The framework supports several types of tests.

### API Tests

These tests verify the proper behavior of API functions, including error
handling. They typically check:

  1. Input parameter validation
  2. Error codes and error propagation
  3. API contract compliance

Example:
[testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c82-129](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c#L82-L129)

### Functional Tests

These tests verify the functional correctness of algorithms by:

  1. Testing against known vectors
  2. Verifying cryptographic properties
  3. Testing various key sizes and modes

Example:
[testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c196-235](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/rsa/test_suite_sdv_eal_rsa_sign_verify.c#L196-L235)

### Integration Tests

These tests verify the integration between components, including:

  1. Provider loading and unloading
  2. Cross-module functionality
  3. End-to-end cryptographic operations

Demo applications are also used for broader integration testing.

Example:
[testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c58-169](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c#L58-L169)

### Performance Tests

These tests measure the performance of cryptographic operations:

  1. Execution time
  2. Memory usage
  3. Scaling characteristics

## Provider Testing

The framework includes specialized support for testing provider modules, which
are dynamically loadable components implementing cryptographic algorithms.

    
    
    Provider Testing
    
    Loading Tests
    
    Algorithm Discovery Tests
    
    Algorithm Implementation Tests
    
    Provider Selection Tests
    
    Dynamic Loading
    
    Path Configuration
    
    Error Handling
    
    Algorithm Query
    
    Capability Enumeration
    
    Correctness Tests
    
    Interoperability Tests
    
    Provider Priority
    
    Attribute-based Selection

Sources:
[testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c58-547](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/sdv/testcase/crypto/provider/test_suite_sdv_eal_provider_load.c#L58-L547)
[crypto/provider/src/mgr/crypt_provider.c37-462](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/src/mgr/crypt_provider.c#L37-L462)

## Continuous Integration

The testing framework is integrated with GitHub Actions for continuous
integration:

  1. Tests are executed on every push to the main branch
  2. Tests are executed for every pull request
  3. Code coverage information is collected and uploaded to Codecov
  4. Test artifacts are preserved for analysis

    
    
    GitHub Push/PR
    
    GitHub Actions Workflow
    
    Build Project
    
    Run Tests
    
    Check ASAN Results
    
    Generate Coverage Report
    
    Run Demo Applications
    
    Upload to Codecov
    
    Pass/Fail Decision

Sources: [.github/workflows/cmake-single-
platform.yml1-53](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/.github/workflows/cmake-
single-platform.yml#L1-L53)

## Best Practices

When writing tests for openHiTLS, follow these best practices:

  1. **Isolation** : Ensure each test is isolated and doesn't depend on the state from other tests
  2. **Completeness** : Test both normal and error paths
  3. **Documentation** : Include clear comments about what each test is verifying
  4. **Memory Management** : Always clean up resources even when tests fail
  5. **Specificity** : Each test should verify a specific aspect of functionality
  6. **Parameterization** : Use test data files for multiple test vectors
  7. **Meaningful Assertions** : Use appropriate assertion macros with clear messages

## Examples

### Example 1: Basic API Test

    
    
    /**
     * @test   SDV_CRYPTO_RSA_SIGN_API_TC001
     * @title  RSA CRYPT_EAL_PkeySign: Wrong parameters.
     * @precon Create the context of the rsa algorithm, set private key and set padding type to pkcsv15
     * @expect Return appropriate error codes for invalid parameters
     */
    void SDV_CRYPTO_RSA_SIGN_API_TC001(Hex *n, Hex *d, int isProvider) {
        // Create context and set up
        CRYPT_EAL_PkeyCtx *pkeyCtx = TestPkeyNewCtx(...);
        ASSERT_TRUE(pkeyCtx != NULL);
        
        // Test invalid parameters
        ASSERT_EQ(CRYPT_EAL_PkeySign(NULL, CRYPT_MD_SHA224, data, dataLen, sign, &signLen), CRYPT_NULL_INPUT);
        // More assertions for other invalid parameter cases
        
        // Cleanup
        CRYPT_EAL_PkeyFreeCtx(pkeyCtx);
    }

### Example 2: Functional Test with Test Vectors

    
    
    /**
     * @test   SDV_CRYPTO_RSA_SIGN_PKCSV15_FUNC_TC002
     * @title  RSA EAL layer signature function test: PKCSV15
     * @expect Signature result matches expected vector
     */
    void SDV_CRYPTO_RSA_SIGN_PKCSV15_FUNC_TC002(int mdId, Hex *n, Hex *d, Hex *msg, Hex *sign, int isProvider) {
        // Set up keys and context
        CRYPT_EAL_PkeyCtx *pkeyCtx = TestPkeyNewCtx(...);
        
        // Sign the message
        ASSERT_EQ(CRYPT_EAL_PkeySign(pkeyCtx, mdId, msg->x, msg->len, signdata, &signLen), CRYPT_SUCCESS);
        
        // Verify against expected signature
        ASSERT_COMPARE("CRYPT_EAL_PkeySign Compare", sign->x, sign->len, signdata, signLen);
        
        // Cleanup
        CRYPT_EAL_PkeyFreeCtx(pkeyCtx);
    }

## Conclusion

The openHiTLS Testing Framework provides a robust and flexible system for
validating the library's functionality and security. By following the patterns
and practices described in this document, developers can effectively write,
execute, and maintain tests that ensure the quality of the openHiTLS library.

# Integration Examples

Relevant source files

  * [config/macro_config/hitls_config_check.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_check.h)
  * [config/macro_config/hitls_config_layer_crypto.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_crypto.h)
  * [config/macro_config/hitls_config_layer_tls.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/config/macro_config/hitls_config_layer_tls.h)
  * [crypto/drbg/include/crypt_drbg.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/drbg/include/crypt_drbg.h)
  * [crypto/eal/src/eal_md.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_md.c)
  * [crypto/eal/src/eal_rand.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/eal/src/eal_rand.c)
  * [crypto/provider/include/crypt_provider.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/crypto/provider/include/crypt_provider.h)
  * [docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/1_Encryption and Integrity Protection Application Development Guide.md)
  * [docs/en/5_Developer Guide/4_provider Development Guide.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer Guide/4_provider Development Guide.md)
  * [docs/index/index.md](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/index/index.md)
  * [include/crypto/crypt_eal_init.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_init.h)
  * [include/crypto/crypt_eal_rand.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/crypto/crypt_eal_rand.h)
  * [include/tls/hitls_config.h](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/include/tls/hitls_config.h)
  * [testcode/demo/CMakeLists.txt](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/CMakeLists.txt)
  * [testcode/demo/client.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c)
  * [testcode/demo/drbg.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c)
  * [testcode/demo/ecdh.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c)
  * [testcode/demo/privpass_token.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c)
  * [testcode/demo/server.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c)
  * [testcode/demo/sm2enc.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2enc.c)
  * [testcode/demo/sm2sign.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c)
  * [testcode/framework/tls/rpc/src/hitls_func.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/framework/tls/rpc/src/hitls_func.c)
  * [tls/config/src/cipher_suite.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/cipher_suite.c)
  * [tls/config/src/config_default.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/config/src/config_default.c)
  * [tls/handshake/pack/src/pack_hello_verify_request.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/handshake/pack/src/pack_hello_verify_request.c)
  * [tls/record/src/rec_write.c](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/tls/record/src/rec_write.c)

This page provides examples and guidance for integrating openHiTLS into
applications. It covers the basic integration patterns, client and server
implementations, cryptographic operations, and the provider framework. For API
reference documentation, see [API
Reference](/openHiTLS/openHiTLS/5.3-assembly-optimizations).

## Basic Integration Steps

Before using openHiTLS in your application, several initialization steps are
required. These steps establish the foundation for secure communication and
cryptographic operations.

    
    
    Application Initialization
    
    Register Memory Functions
    
    Initialize BSL Error Module
    
    Initialize Cryptographic Layer
    
    Initialize Random Number Generator
    
    Initialize Certificate Methods
    
    Application Logic
    
    Cleanup Resources

### 1\. Register Memory Functions

Register memory allocation and deallocation functions using the BSL (Basic
Support Layer) callbacks:

    
    
    BSL_SAL_CallBack_Ctrl(BSL_SAL_MEM_MALLOC_CB_FUNC, malloc);
    BSL_SAL_CallBack_Ctrl(BSL_SAL_MEM_FREE_CB_FUNC, free);

### 2\. Initialize Error Handling

Initialize the error handling module:

    
    
    BSL_ERR_Init();

### 3\. Initialize Cryptographic Layer

Initialize the cryptographic capabilities with the required options:

    
    
    int32_t ret = CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);

### 4\. Initialize Random Number Generator

Set up the random number generator (DRBG):

    
    
    ret = CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);

### 5\. Initialize Certificate and Cryptographic Methods

Register certificate and cryptographic methods:

    
    
    HITLS_CertMethodInit();
    HITLS_CryptMethodInit();

### 6\. Cleanup Resources

When finished, release all allocated resources:

    
    
    HITLS_Close(ctx);
    HITLS_Free(ctx);
    HITLS_CFG_FreeConfig(config);
    CRYPT_EAL_RandDeinit();

Sources:
[testcode/demo/client.c39-56](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L39-L56)
[testcode/demo/server.c43-60](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L43-L60)
[testcode/demo/drbg.c41-58](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c#L41-L58)

## TLS Client Integration

This section demonstrates how to implement a TLS client using openHiTLS. The
example shows establishing a secure connection to a server, sending data, and
receiving a response.

    
    
    ServerNetwork LayerHITLS ClientClient ApplicationServerNetwork LayerHITLS ClientClient Application"HITLS_CFG_NewTLS12Config()""HITLS_CFG_AddCertToStore()""HITLS_New(config)""socket(), connect()""BSL_UIO_New(), BSL_UIO_Ctrl()""HITLS_SetUio(ctx, uio)""HITLS_Connect(ctx)""TLS Handshake""TLS Handshake""HITLS_Write(ctx, data, len)""Encrypted Data""Encrypted Data""Encrypted Response""Encrypted Response""HITLS_Read(ctx, buf, maxLen)""HITLS_Close(ctx)""HITLS_Free(ctx)"

### Client Implementation Example

    
    
    // 1. Create a TLS configuration
    config = HITLS_CFG_NewTLS12Config();
    
    // 2. Load and add certificates to the certificate store
    ret = HITLS_X509_CertParseFile(BSL_FORMAT_ASN1, "ca.der", &rootCA);
    ret = HITLS_X509_CertParseFile(BSL_FORMAT_ASN1, "inter.der", &subCA);
    HITLS_CFG_AddCertToStore(config, rootCA, TLS_CERT_STORE_TYPE_DEFAULT, true);
    HITLS_CFG_AddCertToStore(config, subCA, TLS_CERT_STORE_TYPE_DEFAULT, true);
    
    // 3. Create a TLS context
    ctx = HITLS_New(config);
    
    // 4. Set up network I/O
    uio = BSL_UIO_New(BSL_UIO_TcpMethod());
    ret = BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, sizeof(fd), &fd);
    ret = HITLS_SetUio(ctx, uio);
    
    // 5. Establish a TLS connection
    ret = HITLS_Connect(ctx);
    
    // 6. Send and receive data
    ret = HITLS_Write(ctx, sndBuf, sizeof(sndBuf), &writeLen);
    ret = HITLS_Read(ctx, readBuf, HTTP_BUF_MAXLEN, &readLen);
    
    // 7. Close the connection and free resources
    HITLS_Close(ctx);
    HITLS_Free(ctx);
    HITLS_CFG_FreeConfig(config);
    HITLS_X509_CertFree(rootCA);
    HITLS_X509_CertFree(subCA);
    BSL_UIO_Free(uio);

Sources:
[testcode/demo/client.c82-168](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/client.c#L82-L168)

## TLS Server Integration

This section demonstrates how to implement a TLS server using openHiTLS. The
example shows accepting secure connections, receiving data, and sending
responses.

    
    
    ClientNetwork LayerHITLS ServerServer ApplicationClientNetwork LayerHITLS ServerServer Application"HITLS_CFG_NewTLS12Config()""HITLS_CFG_SetClientVerifySupport()""HITLS_CFG_AddCertToStore()""HITLS_CFG_LoadCertFile(), HITLS_CFG_LoadKeyFile()""HITLS_New(config)""socket(), bind(), listen()""accept()""client socket""BSL_UIO_New(), BSL_UIO_Ctrl()""HITLS_SetUio(ctx, uio)""HITLS_Accept(ctx)""TLS Handshake""TLS Handshake""Encrypted Data""Encrypted Data""HITLS_Read(ctx, buf, maxLen)""HITLS_Write(ctx, data, len)""Encrypted Response""Encrypted Response""HITLS_Close(ctx)""HITLS_Free(ctx)"

### Server Implementation Example

    
    
    // 1. Create a TLS configuration
    config = HITLS_CFG_NewTLS12Config();
    ret = HITLS_CFG_SetClientVerifySupport(config, false);  // disable peer verify
    
    // 2. Load certificates and keys
    ret = HITLS_X509_CertParseFile(BSL_FORMAT_ASN1, "ca.der", &rootCA);
    ret = HITLS_X509_CertParseFile(BSL_FORMAT_ASN1, "inter.der", &subCA);
    HITLS_CFG_AddCertToStore(config, rootCA, TLS_CERT_STORE_TYPE_DEFAULT, true);
    HITLS_CFG_AddCertToStore(config, subCA, TLS_CERT_STORE_TYPE_DEFAULT, true);
    HITLS_CFG_LoadCertFile(config, "server.der", TLS_PARSE_FORMAT_ASN1);
    HITLS_CFG_LoadKeyFile(config, "server.key.der", TLS_PARSE_FORMAT_ASN1);
    
    // 3. Create a TLS context
    ctx = HITLS_New(config);
    
    // 4. Set up network I/O
    uio = BSL_UIO_New(BSL_UIO_TcpMethod());
    ret = BSL_UIO_Ctrl(uio, BSL_UIO_SET_FD, sizeof(fd), &infd);
    ret = HITLS_SetUio(ctx, uio);
    
    // 5. Accept a TLS connection
    ret = HITLS_Accept(ctx);
    
    // 6. Receive and send data
    ret = HITLS_Read(ctx, readBuf, HTTP_BUF_MAXLEN, &readLen);
    ret = HITLS_Write(ctx, sndBuf, sizeof(sndBuf), &writeLen);
    
    // 7. Close the connection and free resources
    HITLS_Close(ctx);
    HITLS_Free(ctx);
    HITLS_CFG_FreeConfig(config);
    HITLS_X509_CertFree(rootCA);
    HITLS_X509_CertFree(subCA);
    HITLS_X509_CertFree(serverCert);
    CRYPT_EAL_PkeyFreeCtx(pkey);
    BSL_UIO_Free(uio);

Sources:
[testcode/demo/server.c94-185](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/server.c#L94-L185)

## Cryptographic Operations Integration

openHiTLS provides a comprehensive set of cryptographic operations that can be
used independently of the TLS protocol. This section demonstrates how to use
these operations in your applications.

    
    
    Cryptographic Layer
    
    Application
    
    Cryptographic Operations
    
    Random Number Generation
    
    Symmetric Encryption/Decryption
    
    Asymmetric Encryption/Decryption
    
    Digital Signatures
    
    Key Exchange
    
    Hash Functions
    
    CRYPT_EAL_RandbytesEx()
    
    CRYPT_EAL_RandSeedEx()
    
    CRYPT_EAL_CipherNewCtx()
    
    CRYPT_EAL_CipherInit()
    
    CRYPT_EAL_CipherUpdate()
    
    CRYPT_EAL_CipherFinal()
    
    CRYPT_EAL_PkeyEncrypt()
    
    CRYPT_EAL_PkeyDecrypt()
    
    CRYPT_EAL_PkeySign()
    
    CRYPT_EAL_PkeyVerify()
    
    CRYPT_EAL_PkeyComputeShareKey()
    
    CRYPT_EAL_MdNewCtx()
    
    CRYPT_EAL_MdUpdate()
    
    CRYPT_EAL_MdFinal()

### Random Number Generation Example

Random number generation is fundamental for many cryptographic operations.
Here's how to generate random numbers:

    
    
    // Initialize random number generator
    ret = CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Generate random bytes
    uint8_t output[100] = {0};
    uint32_t len = 100;
    ret = CRYPT_EAL_RandbytesEx(NULL, output, len);
    
    // Reseed the DRBG
    ret = CRYPT_EAL_RandSeedEx(NULL);
    
    // Cleanup
    CRYPT_EAL_RandDeinit();

Sources:
[testcode/demo/drbg.c61-106](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/drbg.c#L61-L106)

### Digital Signature Example (SM2)

Digital signatures provide authentication and integrity verification:

    
    
    // Create a key context for SM2
    ctx = CRYPT_EAL_PkeyNewCtx(CRYPT_PKEY_SM2);
    
    // Set user ID (required for SM2)
    ret = CRYPT_EAL_PkeyCtrl(ctx, CRYPT_CTRL_SET_SM2_USER_ID, userId, sizeof(userId));
    
    // Initialize random number generator
    ret = CRYPT_EAL_ProviderRandInitCtx(NULL, CRYPT_RAND_SHA256, "provider=default", NULL, 0, NULL);
    
    // Generate a key pair
    ret = CRYPT_EAL_PkeyGen(ctx);
    
    // Sign data
    ret = CRYPT_EAL_PkeySign(ctx, CRYPT_MD_SM3, msg, sizeof(msg), signBuf, &signLen);
    
    // Verify signature
    ret = CRYPT_EAL_PkeyVerify(ctx, CRYPT_MD_SM3, msg, sizeof(msg), signBuf, signLen);
    
    // Cleanup
    CRYPT_EAL_PkeyFreeCtx(ctx);
    CRYPT_EAL_RandDeinit();

Sources:
[testcode/demo/sm2sign.c65-115](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/sm2sign.c#L65-L115)

### Key Exchange Example (ECDH)

Key exchange protocols establish shared secrets between parties:

    
    
    // Create key contexts
    prvCtx = CRYPT_EAL_PkeyNewCtx(CRYPT_PKEY_ECDH);
    pubCtx = CRYPT_EAL_PkeyNewCtx(CRYPT_PKEY_ECDH);
    
    // Set the curve parameters
    ret = CRYPT_EAL_PkeySetParaById(prvCtx, CRYPT_ECC_NISTP256);
    ret = CRYPT_EAL_PkeySetParaById(pubCtx, CRYPT_ECC_NISTP256);
    
    // Set the private key
    prvKey.id = CRYPT_PKEY_ECDH;
    prvKey.key.eccPrv.len = sizeof(prikey);
    prvKey.key.eccPrv.data = prikey;
    ret = CRYPT_EAL_PkeySetPrv(prvCtx, &prvKey);
    
    // Set the public key
    pubKey.id = CRYPT_PKEY_ECDH;
    pubKey.key.eccPub.len = sizeof(pubkey);
    pubKey.key.eccPub.data = pubkey;
    ret = CRYPT_EAL_PkeySetPub(pubCtx, &pubKey);
    
    // Compute the shared key
    shareLen = CRYPT_EAL_PkeyGetKeyLen(prvCtx) / 2;
    shareKey = (uint8_t *)BSL_SAL_Malloc(shareLen);
    ret = CRYPT_EAL_PkeyComputeShareKey(prvCtx, pubCtx, shareKey, &shareLen);
    
    // Cleanup
    CRYPT_EAL_PkeyFreeCtx(prvCtx);
    CRYPT_EAL_PkeyFreeCtx(pubCtx);
    BSL_SAL_Free(shareKey);

Sources:
[testcode/demo/ecdh.c78-152](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/ecdh.c#L78-L152)

## Provider Framework Integration

The provider framework allows plugging in different cryptographic
implementations. This section demonstrates how to use the provider framework
to select and configure cryptographic implementations.

    
    
    Providers
    
    Provider Framework
    
    Application
    
    Provider Framework
    
    Library Context
    
    Provider Management
    
    Algorithm Query
    
    Capabilities
    
    Loading Providers
    
    Unloading Providers
    
    Algorithm Selection
    
    Provider Scoring
    
    TLS Groups
    
    Signature Algorithms
    
    Default Provider
    
    Custom Provider

### Loading and Using Providers

Here's how to load and use providers:

    
    
    // Create a library context
    CRYPT_EAL_LibCtx *libCtx = CRYPT_EAL_LibCtxNew();
    
    // Set the provider loading path
    int ret = CRYPT_EAL_ProviderSetLoadPath(libCtx, "/path/to/providers");
    
    // Load a provider
    CRYPT_EAL_ProvMgrCtx *mgrCtx = NULL;
    ret = CRYPT_EAL_ProviderLoad(libCtx, BSL_SAL_CONVERTER_SO, "provider_name", NULL, &mgrCtx);
    
    // Use the provider for message digest operations
    CRYPT_EAL_MdCTX *ctx = CRYPT_EAL_ProviderMdNewCtx(libCtx, CRYPT_MD_SM3, "attr1=temp_attr1,attr2=temp_attr2");
    
    // Perform operations
    CRYPT_EAL_MdInit(ctx);
    CRYPT_EAL_MdUpdate(ctx, msg->x, msg->len);
    CRYPT_EAL_MdFinal(ctx, output, &outLen);
    
    // Unload the provider
    ret = CRYPT_EAL_ProviderUnload(libCtx, BSL_SAL_CONVERTER_SO, "provider_name");
    
    // Free the library context
    CRYPT_EAL_LibCtxFree(libCtx);

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md462-510](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L462-L510)

### Provider Selection with Attributes

The provider framework supports attribute-based selection for algorithms:

    
    
    // Using the built-in HITLS algorithm library:
    CRYPT_EAL_MdCTX *ctx = CRYPT_EAL_ProviderMdNewCtx(NULL, CRYPT_MD_SM3, "provider=default");
    
    // Searching and initializing with a matching algorithm library in a third-party provider:
    CRYPT_EAL_LibCtx *libCtx = CRYPT_EAL_LibCtxNew();
    int ret = CRYPT_EAL_ProviderSetLoadPath(libCtx, "/path/to/providers");
    ret = CRYPT_EAL_ProviderLoad(libCtx, BSL_SAL_LIB_FMT_SO, "provider_name", NULL, NULL);
    CRYPT_EAL_MdCTX *ctx = CRYPT_EAL_ProviderMdNewCtx(libCtx, CRYPT_MD_SM3, "attr1=temp_attr1,attr2=temp_attr2");
    
    // Mixed usage of third-party providers and HITLS libraries:
    int ret = CRYPT_EAL_ProviderSetLoadPath(NULL, "/path/to/providers");
    ret = CRYPT_EAL_ProviderLoad(NULL, BSL_SAL_LIB_FMT_SO, "provider_name", NULL, NULL);
    CRYPT_EAL_MdCTX *ctx = CRYPT_EAL_ProviderMdNewCtx(NULL, CRYPT_MD_SM3, "attr1=temp_attr1,attr2=temp_attr2");

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md454-492](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L454-L492)

### Provider Scoring Mechanism

The provider framework uses a scoring mechanism to select the most appropriate
provider:

    
    
    // Query with a NULL attribute string, searching by algorithm ID
    ret = CRYPT_EAL_ProviderGetFuncs(libCtx, CRYPT_EAL_OPERAID_HASH, CRYPT_MD_MD5, NULL, &funcs, &provCtx);
    
    // Query with a non-NULL attribute string, matching based on rules
    ret = CRYPT_EAL_ProviderGetFuncs(libCtx, CRYPT_EAL_OPERAID_HASH, CRYPT_MD_MD5, 
        "name=md5,type=hash,version=1.0", &funcs, &provCtx);
    
    // Query with provider scoring mechanism
    ret = CRYPT_EAL_ProviderGetFuncs(libCtx, CRYPT_EAL_OPERAID_HASH, CRYPT_MD_MD5, 
        "name=md5,feature?attr_good,feature?attr_good,feature?attr_bad", &funcs, &provCtx);

Sources: [docs/en/5_Developer Guide/4_provider Development
Guide.md262-279](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/docs/en/5_Developer
Guide/4_provider Development Guide.md#L262-L279)

## Advanced Integration Examples

### Privacy Pass Token Protocol

The privacy pass token protocol provides a way to authenticate users without
revealing their identity:

    
    
    IssuerServerClientIssuerServerClient"tokenChallenge""tokenRequest""tokenResponse""finalToken""verifyToken"

Example implementation:

    
    
    // Create contexts
    client = HITLS_AUTH_PrivPassNewCtx(HITLS_AUTH_PRIVPASS_PUB_VERIFY_TOKENS);
    issuer = HITLS_AUTH_PrivPassNewCtx(HITLS_AUTH_PRIVPASS_PUB_VERIFY_TOKENS);
    server = HITLS_AUTH_PrivPassNewCtx(HITLS_AUTH_PRIVPASS_PUB_VERIFY_TOKENS);
    
    // Set keys
    HITLS_AUTH_PrivPassSetPubkey(client, pubKey, sizeof(pubKey));
    HITLS_AUTH_PrivPassSetPubkey(issuer, pubKey, sizeof(pubKey));
    HITLS_AUTH_PrivPassSetPrvkey(issuer, NULL, privKey, sizeof(privKey));
    HITLS_AUTH_PrivPassSetPubkey(server, pubKey, sizeof(pubKey));
    
    // Generate token challenge (server -> client)
    HITLS_AUTH_PrivPassGenTokenChallenge(server, param, &tokenChallenge);
    HITLS_AUTH_PrivPassSerialization(server, tokenChallenge, tokenChallengeBuff, &tokenChallengeLen);
    
    // Generate token request (client -> issuer)
    HITLS_AUTH_PrivPassGenTokenReq(client, tokenChallenge, &tokenRequest);
    HITLS_AUTH_PrivPassSerialization(client, tokenRequest, tokenRequestBuff, &tokenRequestLen);
    
    // Generate token response (issuer -> client)
    HITLS_AUTH_PrivPassGenTokenResponse(issuer, tokenRequest, &tokenResponse);
    HITLS_AUTH_PrivPassSerialization(client, tokenResponse, tokenResponseBuff, &tokenResponseLen);
    
    // Generate final token (client -> server)
    HITLS_AUTH_PrivPassGenToken(client, tokenChallenge, tokenResponse, &finalToken);
    HITLS_AUTH_PrivPassSerialization(client, finalToken, finalTokenBuff, &finalTokenLen);
    
    // Verify token (server)
    HITLS_AUTH_PrivPassVerifyToken(server, tokenChallenge, finalToken);

Sources:
[testcode/demo/privpass_token.c218-342](https://github.com/openHiTLS/openHiTLS/blob/d4dca345/testcode/demo/privpass_token.c#L218-L342)

## Conclusion

This page has demonstrated various integration patterns for openHiTLS,
including basic setup, client and server implementations, cryptographic
operations, and provider framework usage. These examples can be adapted to
different application requirements, providing a foundation for secure
communication and cryptographic operations.

Remember to properly initialize the library, handle errors, and clean up
resources to ensure secure and reliable operation of openHiTLS in your
applications.

